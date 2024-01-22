<template>
  <h1>Результати пошуку:</h1>
  <h3>{{ product.name }}</h3>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      product: {},
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
          this.product = response.data;
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
