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
// axios.defaults.baseURL = "https://lionfish-app-n5fr2.ondigitalocean.app";
// axios.defaults.headers.common = {"Access-Control-Allow-Origin" : "*"}

// Add a request interceptor to include CORS headers
// axios.interceptors.request.use(function (config) {
//   config.headers["Access-Control-Allow-Methods"] = "GET,POST";
//   config.headers["Access-Control-Allow-Origin"] = "*";
//   config.headers["Access-Control-Allow-Credentials"] = "true";
//   config.headers["Access-Control-Allow-Headers"] = "Access-Control-Allow-Headers, *,Accept, X-Requested-With, *, Access-Control-Request-Method, Access-Control-Request-Headers"
//   config.headers["Access-Control-Expose-Headers"] = "*";
//   return config;
// });
// axios.defaults.headers.common = {
// 'Access-Control-Allow-Methods': 'GET,POST',
// 'Access-Control-Allow-Origin': '',
// 'Access-Control-Allow-Credentials': 'true',
// 'Access-Control-Allow-Headers': '',
// 'Access-Control-Expose-Headers': '*',
// }
axios.defaults.baseURL = "https://lionfish-app-n5fr2.ondigitalocean.app";

const app = createApp(App);

app.use(router, axios);

app.mount("#app");
