<script>
// import TheWelcome from "../components/TheWelcome.vue";
// import MenuView from "./MenuView.vue";
</script>

<template>
  <main>
    <img alt="banner" src="../assets/pict2.jpg" width="1329px" height="533px" />
  </main>
</template>
<!-- <template>
  <main>
    <swiper :options="swiperOptions">
      <swiper-slide v-for="(image, index) in images" :key="index">
        <img
          v-bind:src="image.src"
          :alt="image.alt"
          width="1329px"
          height="533px"
        />
      </swiper-slide>
    </swiper>
  </main>
</template>

<script>
import { ref, onMounted } from "vue";
import { Swiper, SwiperSlide } from "vue-awesome-swiper";

export default {
  components: {
    Swiper,
    SwiperSlide,
  },

  data() {
    return {
      swiperOptions: {
        navigation: {
          nextEl: ".swiper-button-next", // Класс элемента "следующий слайд"
          prevEl: ".swiper-button-prev", // Класс элемента "предыдущий слайд"
        },
        autoplay: {
          delay: 2000,
          disableOnInteraction: false,
        },
      },
      images: [
        { src: "../assets/pict1.jpg", alt: "Slide_1" },
        { src: "../assets/pict2.jpg", alt: "Slide 2" },
        { src: "../assets/pict3.jpg", alt: "Slide 3" },
      ],
    };
  },

  // Хук монтирования компонента
  mounted() {
    // this.swiperOptions.autoplay = {
    //   delay: 2000,
    //   disableOnInteraction: false,
    // };
  },
};
</script> -->

<style scoped></style>
