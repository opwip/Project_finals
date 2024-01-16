<template>
  <div>
    <RouterLink
      :to="{ name: 'CategoryPage', params: { categoryId: category.id } }"
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
