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
  border-radius: 5px;
  min-height: 26vw;
  min-width: 23vw;
  padding: 3vw 2vw;
  /* font-weight: bold; */
  margin: 0 3.2vw;
  display: flex;
  align-self: flex-start;
  align-items: flex-start;
}
li {
  list-style: none;
  line-height: 7vw;
  font-size: 10vw;
}
li a {
  list-style: none;
  color: var(--vt-c-text-light-2);
  font-size: 10vw;
  /* font-weight: bold; */
  text-transform: uppercase;
}
@media (max-width: 1540px) {
  li {
    font-size: 10%;
  }
}
@media (max-width: 650px) {
  aside {
    min-width: 70vw;
  }
}
</style>
