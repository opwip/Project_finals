<template>
  <aside>
    <CategoryMenu :categories="categories" />
  </aside>
</template>

<script>
import axios from "axios";
import CategoryMenu from "../components/CategoryMenu.vue";

export default {
  components: {
    CategoryMenu,
  },
  data() {
    return {
      categories: [],
    };
  },
  mounted() {
    this.fetchCategories();
  },
  methods: {
    fetchCategories() {
      axios
        .get("/api/categories")
        .then((response) => {
          this.categories = response.data;
          console.log("Что мы получяем:", response.data);
          console.log(this.categories);
        })
        .catch((error) => {
          console.error("Если вдруг у нас ошибка:", error);
        });
    },
  },
};
</script>

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
