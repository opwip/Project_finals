<template>
  <div>
    <RouterLink
      :to="{
        name: 'CategoryPage',
        params: { categoryId: category.id },
        query: { categoryName: category.name },
      }"
      v-for="category in categories"
      :key="category.id"
    >
      <h2>{{ category.name }}</h2>
    </RouterLink>
  </div>
</template>

<script>
export default {
  props: {
    categories: {
      type: Array,
      required: true,
    },
  },
};
</script>
<style>
a.router-link-exact-active {
  color: var(--vt-c-indigo);
}
@media (max-width: 1865px) {
  a {
    font-size: 0.8vw;
  }
}
</style>
