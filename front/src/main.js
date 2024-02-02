import "./assets/main.css";
// import Swiper from "swiper/bundle";
// import Swiper from "swiper";
// import "swiper/swiper-bundle.css";
// import "swiper/css/swiper.css";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import axios from "axios";

axios.defaults.baseURL = "https://lionfish-app-n5fr2.ondigitalocean.app";

const app = createApp(App);

app.use(router, axios);

app.mount("#app");
