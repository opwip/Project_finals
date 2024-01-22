<template>
  <div>
    <h1>{{ productName }}</h1>
    <div class="item-page-wrap">
      <div class="top-info-block">
        <div class="cart-img">
          <img
            v-bind:src="product.photo"
            alt="filter-image"
            width="380px"
            height="380px"
          />
        </div>

        <div class="item-info">
          <!-- <h4>{{ product.name }}</h4> -->
          <p class="storage">
            <span v-if="product.in_stock == true" style="color: greenyellow"
              >В наявності</span
            >
            <span v-else style="color: red">Немає в наявності</span>
          </p>
          <p class="item-price">
            Ціна: <span>{{ product.price }}</span> грн.
          </p>
          <div class="basket">
            <p>Додати у кошик</p>
            <button>
              <img
                src="../assets/basket.png"
                alt=""
                width="45px"
                height="40px"
              />
            </button>
          </div>
        </div>
      </div>
      <div class="descript">
        <h2>Опис:</h2>
        <br />
        <p>{{ product.desc }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      product: {},
      productName: null,
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
      const productId = this.$route.params.productId;
      const productName = this.$route.query.productName;
      console.log(productId);
      console.log(productName);
      this.getProduct(productId, productName);
    },
    getProduct(productId, productName) {
      axios
        .get(`api/product/${productId}`)
        .then((response) => {
          this.product = response.data;
          this.productName = productName;
          console.log(response.data);
          const baseUrl = "http://127.0.0.1:8000/";
          this.product.photo = baseUrl + this.product.photo;
          const photo = this.product.photo;
          console.log(photo);
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
<style scoped>
h1,
h2,
span {
  font-weight: bold;
}
.item-page-wrap {
  width: 80%;
  margin-top: 2rem;
  display: flex;
  gap: 35px;
  flex-wrap: wrap;
}
.top-info-block {
  width: 100%;
  display: flex;
  gap: 70px;
}
.item-info {
  margin-top: 9rem;
  border-radius: 4px;
  width: 25%;
  height: 13vw;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
.item-info h4 {
  text-align: center;
  color: var(--vt-c-text-light-1);
  margin-bottom: 1rem;
}
.cart-img {
  margin: 0;
  width: 370px;
  height: 370px;
}
.storage span {
  font-size: 1rem;
}
.item-price span {
  font-size: 1.1rem;
  color: var(--vt-c-text-light-1);
}
.basket {
  width: 100%;
  margin-top: 10px;
  display: flex;
  align-items: center;
  gap: 30px;
  font-size: 1rem;
}
/* .basket button {
  background-color: var(--vt-c-text-light-1);
} */
.basket button img {
  height: 35px;
  width: 35px;
  border-radius: 5%;
}
/* .basket img {
  color: white;
} */
.descript {
  width: 70%;
}
</style>
