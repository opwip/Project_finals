<script>
export default {
  data() {
    return {
      input: "",
    };
  },
};
</script>

<template>
  <label for="search">
    <RouterLink
      :to="{
        name: 'SearchView',
        query: { searchValue: input },
      }"
    >
      <input v-model="input" id="search" />
      <img
        alt="Search icon"
        src="../assets/search@2x.png"
        width="26px"
        height="26px"
      />
    </RouterLink>
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
  border: 1px solid lightgrey;
  border-radius: 5px;
  height: 2.6rem;
  width: 15rem;
  /* margin: 0.2rem 0 0 0.5rem; */
  display: block;
  position: relative;
}
label img {
  color: lightgrey;
  position: absolute;
  top: 0.5rem;
  right: 0.8rem;
  opacity: 0.5;
}

@media (max-width: 650px) {
  label img {
    top: 0.2rem;
    right: 0.4rem;
    width: 0.8rem;
    height: 1rem;
  }
}
</style>
