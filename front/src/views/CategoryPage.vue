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
                width="230px"
                height="210px"
              />
            </div>
          </RouterLink>
          <div class="item-footer">
            <div>
              <p>
                Ціна: <span>{{ product.price }}</span> грн.
              </p>
              <p class="storage">
                <span v-if="product.in_stock == true" style="color: greenyellow"
                  >В наявності</span
                >
                <span v-else style="color: red">Немає в наявності</span>
              </p>
            </div>
  
            <button v-if="product.in_stock == true" @click="addToBasket(product)">
              <img src="../assets/basket.png" alt="" width="40px" height="35px" />
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
      addToBasket(product) {
        const BasketItem = {
          id: product.id,
          name: product.name,
          photo: product.photo,
          price: product.price,
          amount: 1,
        };
        // });
        const currentBasketItems = JSON.parse(localStorage.getItem("cart")) || [];
  
        currentBasketItems.push(BasketItem);
  
        localStorage.setItem("cart", JSON.stringify(currentBasketItems));
        console.log(currentBasketItems);
        alert("Товар додан у кошик!");
      },
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
    margin-bottom: 2rem;
  }
  .cart-img {
    display: flex;
    justify-content: center;
  }
  .item-footer {
    width: 100%;
    margin-top: 10px;
    display: flex;
    align-items: center;
    /* gap: 50px; */
    justify-content: space-around;
    padding: 0 15px;
  }
  .storage span {
    font-size: 1rem;
  }
  </style>