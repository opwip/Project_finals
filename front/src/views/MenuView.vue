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
  <aside >
    <!-- <h2>Меню</h2> -->
    <ul >
      <li v-for="category in categories"
    v-bind:key = 'category.id'><MenuItem :msg="category.name" /></li>
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

<script>
import axios from "axios"

export default {
  data(){
    return{
      categories: []
    }
  },
  mounted() {
    console.log('mounted')

    axios
      .get ('/api/list/')
      .then (response => {
        console.log(response.data)

        this.categories = response.data
      })
  }
}
</script>