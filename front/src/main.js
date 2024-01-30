import "./assets/main.css";
// import Swiper from "swiper/bundle";
// import Swiper from "swiper";
// import "swiper/swiper-bundle.css";
// import "swiper/css/swiper.css";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import axios from "axios";
// import VueAwesomeSwiper from "vue-awesome-swiper";
// Vue.use(VueAwesomeSwiper);

axios.defaults.baseURL = "http://127.0.0.1:8000";

const app = createApp(App);

app.use(router, axios);

app.mount("#app");
