<template>
  <div>
    <h2 v-if="category">{{ category.name }} Товари:</h2>
    <!-- <div class="stafPageyWrap">
      <div class="itemCart" v-for="product in category.products" :key="product.id">
        {{ product.name }} - {{ product.price }}
      </div>
    </div> -->
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      category: {},
    };
  },
  created() {
    // Здесь используем маршрутизацию для получения categoryId из URL
    // и затем делаем запрос к серверу, чтобы получить товары этой категории
    const categoryId = this.$route.params.categoryId;
    console.log(categoryId);
    this.fetchCategory(categoryId);
  },
  methods: {
    fetchCategory(categoryId) {
      // Здесь делаем GET-запрос к серверу для получения товаров по categoryId
      axios
        .get(`/api/list/${categoryId}/products`)
        .then((response) => {
          this.category = response.data;

          console.log(response.data);
        })
        .catch((error) => {
          console.error("Ошибка при получении данных:", error);

          console.log("Статус ответа:", error.response.status);
          console.log("Статус данніх:", error.response.data);
        });
    },
  },
};
</script>
