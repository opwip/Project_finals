<script setup>
import { ref } from "vue";
import MenuItem from "../components/MenuItem.vue";

const Cat1 = ref("Проточні Фільтри");
const Cat2 = ref("Питні Фільтри");
const Cat3 = ref("Змінні Картриджи");
const Cat4 = ref("Комплектуючі");
const Cat5 = ref("Битові фільтри");
</script>

<template>
  <aside>
    <!-- <h2>Меню</h2> -->
    <ul>
      <li><MenuItem :msg="Cat1" /></li>
      <li><MenuItem :msg="Cat2" /></li>
      <li><MenuItem :msg="Cat3" /></li>
      <li><MenuItem :msg="Cat4" /></li>
      <li><MenuItem :msg="Cat5" /></li>
      <li><MenuItem :msg="Cat3" /></li>
      <li><MenuItem :msg="Cat4" /></li>
      <li><MenuItem :msg="Cat5" /></li>
      <li><MenuItem :msg="Cat4" /></li>
      <li><MenuItem :msg="Cat5" /></li>
    </ul>
  </aside>
</template>
<style scoped>
aside {
  border: 1px solid lightgrey;
  height: 100%;
  min-width: 21rem;
  padding: 3rem 2rem;
  font-weight: bold;
  margin: 0 5rem;
  display: flex;
  align-self: flex-start;
  align-items: flex-start;
}
li {
  list-style: none;
  line-height: 30px;
  /* color: var(--vt-c-text-light-2);
  font-size: 16px;
  font-weight: bold;
  text-transform: uppercase; */
}
li a {
  list-style: none;
  color: var(--vt-c-text-light-2);
  font-size: 16px;
  font-weight: bold;
  text-transform: uppercase;
}
</style>
