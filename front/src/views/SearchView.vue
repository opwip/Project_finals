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
      </RouterLink>
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
      const productName = this.$route.query.searchValue;
      console.log(productName);
      if (productName) {
        this.getProduct(productName);
      }
    },
    getProduct(productName) {
      axios
        .get(`api/search/?search=${productName}`)
        .then((response) => {
          this.products = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.error("Помилка при отриманні даних:", error);
        });
    },
  },
};
</script>

<style scoped>
h1 {
  margin-bottom: 2rem;
}
h4 {
  margin: 2rem 0;
  color: brown;
  font-weight: bold;
}
</style>
