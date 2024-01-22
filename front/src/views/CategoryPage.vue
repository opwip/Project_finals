<template>
  <div>
    <h1>{{ categoryName }}</h1>
    <div class="goods-page-wrap">
      <div class="item-cart" v-for="product in category" :key="product.id">
        <RouterLink
          :to="{
            name: 'GoodsItemPage',
            params: { productId: product.id },
            query: { productName: product.name },
          }"
        >
          <h4>{{ product.name }}</h4>
          <div class="cart-img">
            <img
              v-bind:src="product.photo"
              alt="filter-image"
              width="260px"
              height="240px"
            />
          </div>
        </RouterLink>
        <div class="price">
          <p>
            Ціна: <span>{{ product.price }}</span> грн.
          </p>
          <button>
            <img src="../assets/basket.png" alt="" width="45px" height="40px" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      category: [],
      categoryName: null,
    };
  },

  watch: {
    $route: "getData",
  },
  created() {
    this.getData();
  },
  methods: {
    getData() {
      const categoryId = this.$route.params.categoryId;
      const categoryName = this.$route.query.categoryName;
      console.log(categoryId);
      console.log(categoryName);
      this.getCategory(categoryId, categoryName);
    },
    getCategory(categoryId, categoryName) {
      axios
        .get(`/api/products/?category=${categoryId}`)
        .then((response) => {
          this.category = response.data;
          this.categoryName = categoryName;
          console.log(response.data);
        })
        .catch((error) => {
          console.error("Помилка при отриманні даних:", error);

          // console.log("Статус ответа:", error.response.status);
          // console.log("Статус данніх:", error.response.data);
        });
    },
  },
};
</script>
<style scope>
h1,
/* h2, */
h4,
p span {
  font-weight: bold;
}
.goods-page-wrap {
  width: 100%;
  margin-top: 2rem;
  display: flex;
  gap: 40px;
  flex-wrap: wrap;
}
.item-cart {
  /* border: 1px solid lightgray;
  border-radius: 4px; */
  width: 16vw;
  height: 22vw;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
.item-cart h4 {
  text-align: center;
  color: var(--vt-c-text-light-1);
  margin-bottom: 1rem;
}
.cart-img {
  margin: 0 auto;
  /* width: 270px;
  height: 270px; */
  /* border: 1px dotted blue; */
}
.price {
  width: 100%;
  margin-top: 10px;
  display: flex;
  align-items: center;
  /* gap: 50px; */
  justify-content: space-around;
  padding: 0 15px;
}
/* .price button {
  border: 1px solid lightblue;
} */
/* button {
  border: 1px solid lightgray;
} */
</style>
