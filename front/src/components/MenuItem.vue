<script setup>
import { reactive } from "vue";

const prop = defineProps({
  msg: String,
  required: true,
});

const itemCart = reactive({});

itemCart.value = {
  id: 1,
  name: "Категория 2",
  //   items: [
  //     { id: 1, name: "Товар 1", price: 10 },
  //     { id: 2, name: "Товар 2", price: 15 },
  //   ],
};
// function setCategory(newName) {
//   itemCart.value.name = newName;
// }
// setCategory("Проточні фільтри");
</script>

<template>
  <a href="#">{{ msg }}</a>
</template>

<style scoped>
a:hover {
  color: var(--color-heading);
  /* font-weight: bold; */
}
</style>
