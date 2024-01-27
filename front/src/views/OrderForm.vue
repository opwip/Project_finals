<template>
  <div class="form-wrap">
    <div class="form-headers">
      <h2>Форма замовлення</h2>
      <legend><h3>Данні покупця</h3></legend>
    </div>
    <div class="order-form">
      <div class="form-item">
        <label for="name">Ім'я</label>
        <input v-model="name" id="name" placeholder="Ваше ім'я" />
      </div>
      <div class="form-item">
        <label for="surname">Прізвище</label>
        <input v-model="surname" id="surname" placeholder="Ваше прізвище" />
      </div>
      <div class="form-item">
        <label for="email">Електронна адреса </label>
        <input v-model="email" id="mail" placeholder="Ваш email" />
      </div>
      <div class="form-item">
        <label for="phone">Телефон</label>
        <input v-model="phone" id="phone" placeholder="Ваш номер телефону" />
      </div>
      <button @click="sendUserData">Далі</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      name: "",
      surname: "",
      email: "",
      phone: "",
      basketItems: {},
    };
  },
  created() {
    this.getBasket();
  },
  methods: {
    getBasket() {
      const storedBasket = localStorage.getItem("cart");
      if (storedBasket) {
        this.basketItems = JSON.parse(storedBasket);
      }
    },
    async sendUserData() {
      try {
        let nameRegEx = /^[а-яА-я]{3,10}$/;
        let mailRegEx = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,10}$/;
        let phoneRegEx = /^[0-9]{10,12}$/;
        let testMail = mailRegEx.test(this.email);
        let testName = nameRegEx.test(this.name);
        let testSurName = nameRegEx.test(this.surname);
        let testPhone = phoneRegEx.test(this.phone);
        if (!this.name || !this.surname || !this.email || !this.phone) {
          console.error("Заповнені не всі поля форми");
          alert("Будь ласка, заповніть всі поля форми.");
          return;
        } else if (!testMail) {
          alert("Будь ласка, внесіть корректно свою електронну адресу.");
          return;
        } else if (!testName) {
          alert("Будь ласка, внесіть корректно своє ім'я.");
          return;
        } else if (!testSurName) {
          alert("Будь ласка, внесіть корректно своє прізвище.");
          return;
        } else if (!testPhone) {
          alert("Будь ласка, внесіть корректно свій номер телефону.");
          return;
        }
        // Получаем данные из формы и из корзины
        const formData = {
          name: this.name,
          surname: this.surname,
          email: this.email,
          phone: this.phone,
          basket: this.basketItems,
        };

        // Отправляем данные на сервер
        const response = await axios.post("api/order/", formData);

        // Обработываем ответ от сервера
        console.log("Відповідь сервера:", response.data);
        console.log("MNOTHIG", this.basketItems)
      } catch (error) {
        console.error("Помилка при надсиланні даних:", error.response || error);
      }
    },
  },
};
</script>

<style scoped>
/* .form-wrap {
  display: flex;
  flex-direction: column;
} */
.order-form {
  display: flex;
  flex-direction: row;
  gap: 2rem;
  flex-wrap: wrap;
  width: 37vw;
  margin-top: 1.5rem;
}

.form-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  width: 330px;
}
.form-item input {
  height: 40px;
}
.form-item input {
  height: 40px;
}
/* form-item input ::placeholder {
  font-style: italic;
} */
.form-headers h2 {
  margin-bottom: 2rem;
}
.form-headers h3 {
  font-weight: bold;
}
.order-form button {
  width: 70px;
  height: 25px;
  margin-left: auto;
  margin-right: 2rem;
}
</style>
