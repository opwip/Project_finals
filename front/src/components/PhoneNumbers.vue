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
<<<<<<< HEAD
    <img alt="Phone icon" src="@/assets/tel.png" width="25px" height="30px" />
=======
    <img alt="Phone icon" src="../assets/tel.png" width="25px" height="30px" />
>>>>>>> 914d682ceb1f4a85c1d5435e814baddfeafa912a
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
