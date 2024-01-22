<template>
  <div class="search-page-wrap">
    <h1>Результати пошуку:</h1>
    <div class="item-cart" v-for="product in products" :key="product.id">
      <RouterLink
        :to="{
          name: 'GoodsItemPage',
          params: { productId: product.id },
          query: { productName: product.name },
        }"
      >
        <h4>{{ product.name }}</h4>
        <!-- <div class="cart-img">
          <img
            v-bind:src="product.photo"
            alt="filter-image"
            width="260px"
            height="240px"
          />
        </div> -->
      </RouterLink>
      <!-- <div class="price">
        <p>
          Ціна: <span>{{ product.price }}</span> грн.
        </p>
        <button>
          <img src="../assets/basket.png" alt="" width="45px" height="40px" />
        </button>
      </div> -->
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      products: [],
      searchValue: "",
    };
  },

  watch: {
    "$route.query": "getData",
  },
  created() {
    this.getData();
  },
  methods: {
    getData() {
      // const productId = this.$route.params.productId;
      const productName = this.$route.query.searchValue;
      console.log(productName);
      this.getProduct(productName);
    },
    getProduct(productName) {
      axios
        .get(`api/search/?search=${productName}`)
        .then((response) => {
          this.products = response.data;
          // this.productName = productName;
          console.log(response.data);
        })
        .catch((error) => {
          console.error("Помилка при отриманні даних:", error);

          //   console.log("Статус ответа:", error.response.status);
          //   console.log("Статус данніх:", error.response.data);
        });
    },
  },
};
</script>

<style scoped></style>
