import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
// import SearchView from "../views/SearchView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: " ",
      component: HomeView,
    },

    {
      path: "/delivery",
      name: "delivery",
      component: () => import("../views/DeliveryView.vue"),
    },
    {
      path: "/payment",
      name: "payment",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/PaymentView.vue"),
    },
    {
      path: "/guarantee",
      name: "guarantee",
      component: () => import("../views/GuaranteeView.vue"),
    },
    {
      path: "/search",
      name: "SearchView",
      component: () => import("../views/SearchView.vue"),
    },
    {
      path: "/basket",
      name: "basket",
      component: () => import("../views/BasketView.vue"),
    },
    {
      path: "/category/:categoryId",
      name: "CategoryPage",
      component: () => import("../views/CategoryPage.vue"),
    },
    {
      path: "/product/:productId",
      name: "GoodsItemPage",
      component: () => import("../views/GoodsItemPage.vue"),
    },
    {
      path: "/orderForm",
      name: "OrderForm",
      component: () => import("../views/OrderForm.vue"),
    },
  ],
});

export default router;
