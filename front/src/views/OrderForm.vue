<template>
  <div class="form-wrap">
    <div class="form-headers">
      <h2>Форма замовлення</h2>
      <legend><h3>Данні покупця</h3></legend>
    </div>
    <div class="order-form">
      <div class="form-item">
        <label for="name">Ім'я <span>*</span></label>
        <input v-model="name" id="name" placeholder="Ваше ім'я" />
      </div>
      <div class="form-item">
        <label for="surname">Прізвище <span>*</span></label>
        <input v-model="surname" id="surname" placeholder="Ваше прізвище" />
      </div>
      <div class="form-item">
        <label for="email">Електронна адреса <span>*</span></label>
        <input v-model="email" id="mail" placeholder="Ваш email" />
      </div>
      <div class="form-item">
        <label for="phone">Телефон <span>*</span></label>
        <input
          v-model="phone"
          id="phone"
          placeholder="Ваш номер телефону +380..."
        />
      </div>
      <button class="confirm-btn" @:click="sendUserData">Далі</button>
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
        let nameRegEx = /^[А-Яа-яёЁЇїІіЄєҐґ]{3,12}$/;
        let mailRegEx = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,10}$/;
        let phoneRegEx = /^\+380[1-9]{1}\d{8}$/;
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
        const formData = {
          name: this.name,
          surname: this.surname,
          email: this.email,
          phone: this.phone,
          basket: this.basketItems,
        };
        this.$router.push({ name: "OrderConfirm" });

        this.clearBasket("cart");
        // на сервер
        const response = await axios.post("api/order/", formData);

        // ловим ответ
        console.log("Відповідь сервера:", response.data);
        console.log("MNOTHIG", this.basketItems);
      } catch (error) {
        console.error("Помилка при надсиланні даних:", error.response || error);
      }
    },
    clearBasket() {
      localStorage.clear("cart");
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
  position: relative;
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
.form-item span {
  color: red;
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
.confirm-btn {
  width: 70px;
  height: 25px;
  position: absolute;
  right: 2rem;
  top: 15rem;
}
</style>
