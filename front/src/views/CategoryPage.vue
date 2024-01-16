<template>
  <div>
    <h2>{{ category.name }}Товари:</h2>
    <!-- <div class="stafPageyWrap">
      <div class="itemCart" v-for="product in category.products" :key="product.id">
        {{ product.name }} - {{ product.price }}
      </div>
    </div> -->
  </div>
</template>

<script>
export default {
  data() {
    return {
      category: [],
    };
  },
  //   created() {
  //     // Здесь используем маршрутизацию для получения categoryId из URL
  //     // и затем делаем запрос к серверу, чтобы получить товары этой категории
  //     const categoryId = this.$route.params.categoryId;
  //     this.fetchCategory(categoryId);
  //   },
  //   methods: {
  //     fetchCategory(categoryId) {
  //       // Здесь делаем GET-запрос к серверу для получения товаров по categoryId
  //       axios
  //         .get(`/api/list/${categoryId}/products`)
  //         .then((response) => {
  //           this.category.products = response.data;
  //         })
  //         .catch((error) => {
  //           console.error("Ошибка при получении данных:", error);
  //         });
  //     },
  //   },
};
</script>
