<script setup></script>

<template>
  <label for="search">
    <input id="search" />
    <img
      alt="Search icon"
      src="../assets/search@2x.png"
      width="26px"
      height="26px"
    />
  </label>
</template>

<style scoped>
input {
  border: none;
  font-size: 16px;
}
input:active,
:hover,
:focus {
  outline: 0;
  outline-offset: 0;
}
label {
  border: 2px solid lightgrey;
  border-radius: 5px;
  height: 2.5rem;
  width: 15rem;
  /* margin: 0.2rem 0 0 0.5rem; */
}
</style>
