import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import MenuItem from "../components/MenuItem.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/home",
      name: "home",
      component: HomeView,
    },
    {
      path: "/menu-item",
      name: "menu-item",
      component: MenuItem,
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
  ],
});

export default router;
