<script setup>
defineProps({
  msg: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <div class="greetings">
    <img alt="Phone icon" src="@/assets/tel.png" width="25px" height="30px" />
    <h2 class="main-color">{{ msg }}</h2>
  </div>
</template>

<style scoped>
.greetings {
  display: flex;
  gap: 10px;
  justify-content: space-between;
}
</style>
