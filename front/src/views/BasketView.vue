<template>
  <div class="wrap">
    <h1>Кошик товарів</h1>
    <div v-if="basketItems.length === 0">
      <h3>Ваш кошик пустий</h3>
    </div>
    <div v-else class="basket-items">
      <table>
        <tr>
          <th>ЗОБРАЖЕННЯ</th>
          <th>НАЗВА ТОВАРУ</th>
          <th>КІЛЬКІСТЬ</th>
          <th>ЦІНА</th>
          <th>ЗАГАЛЬНА ВАРТІСТЬ</th>
        </tr>
        <tr v-for="item in basketItems" :key="item.id">
          <td>
            <img
              v-bind:src="item.photo"
              alt="filter-image"
              width="50px"
              height="50px"
            />
          </td>
          <td>
            <RouterLink
              :to="{
                name: 'GoodsItemPage',
                params: { productId: item.id },
                query: { productName: item.name },
              }"
            >
              <h4>{{ item.name }}</h4>
            </RouterLink>
          </td>
          <td>
            <!-- <label for="amount">Кількість:</label> -->
            <input
              type="number"
              id="amount"
              v-model="item.amount"
              @input="updateAmount"
              min="1"
            />
          </td>
          <td class="price">{{ item.price }} грн</td>
          <td class="price">{{ calculateTotal(item) }} грн</td>
          <td>
            <button @click="removeFromCart(item.id)" class="delete">Х</button>
          </td>
        </tr>
      </table>

      <h3 class="price">Разом: {{ calculateTotal() }} грн.</h3>
      <RouterLink to="/">Продовжити покупки</RouterLink>
      <RouterLink
        :to="{
          name: 'OrderForm',
          // params: { itemId: item.id },
          // query: { Name: item.name },
        }"
      >
        <h4>Оформити замовлення</h4>
      </RouterLink>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      basketItems: [],
    };
  },
  mounted() {
    this.getBasket();
  },
  methods: {
    getBasket() {
      const storedBasket = JSON.parse(localStorage.getItem("cart")) || [];
      this.basketItems = storedBasket;
      console.log(storedBasket);
    },

    removeFromCart(itemId) {
      // Находим индекс товара в корзине
      const index = this.basketItems.findIndex((item) => item.id === itemId);

      if (index !== -1) {
        // Удаляем товар из корзины по индексу
        this.basketItems.splice(index, 1);
      }
      this.updateLocalStorage();
    },
    updateAmount(itemId, newAmount) {
      // Находим товар в корзине по id
      const item = this.basketItems.find((item) => item.id === itemId);

      if (item) {
        // Обновляем количество товара
        item.amount = newAmount;
      }
      this.updateLocalStorage();
    },
    calculateTotal(item) {
      // Если передан конкретный товар, возвращаем его общую стоимость
      if (item) {
        return item.amount * item.price;
      }
      // Если не передан товар, вычисляем общую стоимость корзины
      return this.basketItems.reduce((total, currentItem) => {
        return total + currentItem.amount * currentItem.price;
      }, 0);
    },
    updateLocalStorage() {
      // Обновляем Local Storage после изменений в корзине
      localStorage.setItem("cart", JSON.stringify(this.basketItems));
    },
  },
};
</script>

<style scoped>
.wrap {
  min-width: 45vw;
}
.wrap h1 {
  margin-bottom: 2rem;
}
table {
  border-collapse: collapse;
  text-align: center;
}
table tr td,
th {
  border: 1px solid lightgray;
  padding: 5px;
}
table th {
  font-weight: bold;
  padding: 7px;
}
table input {
  width: 35px;
  height: 25px;
}
.price {
  color: var(--vt-c-text-light-1);
  font-weight: bold;
}
.delete {
  height: 22px;
  width: 22px;
  background-color: #dc362e;
  color: white;
  border: 1px solid white;
  border-radius: 50%;
}
.wrap h3 {
  margin: 2rem 3rem 0 0;
  text-align: end;
}
</style>

<!-- v-for="item in basketItems"
:key="item.id"
:item="item"
@remove="removeFromCart"
@updateAmount="updateAmount" -->
