<script setup>
import { RouterLink, RouterView } from "vue-router";
import PhoneNumbers from "./components/PhoneNumbers.vue";
import MenuViewVue from "./views/MenuView.vue";
import SearchInput from "./components/SearchInput.vue";
</script>

<template>
  <header>
    <img
      alt="Vue logo"
      class="logo"
      src="./assets/logo22.jpg"
      width="208"
      height="89"
    />

    <div class="header-menu-wrap">
      <nav>
        <RouterLink to="/">Головна</RouterLink>
        <RouterLink to="/payment">Оплата</RouterLink>
        <RouterLink to="/delivery">Доставка</RouterLink>
        <RouterLink to="/guarantee">Гарантія</RouterLink>
      </nav>
      <div class="info-tools-wrap">
        <PhoneNumbers msg="(093)111-22-33, (067)123-45-67" />
        <SearchInput />
        <RouterLink to="/basket">
          <div class="basket-btn">
            <img src="./assets/basket.png" alt="" width="35px" height="30px" />
          </div>
        </RouterLink>
      </div>
    </div>
  </header>
  <div class="main-content-wrap">
    <MenuViewVue />
    <RouterView />
  </div>
  <footer>
    <img src="./assets/Copy2.png" alt="" width="13px" height="13px" />
    <h4>Created by Medvediev & Kolesnyk - 2024</h4>
  </footer>
</template>

<style>
/* #app {
  display: flex;

  flex-wrap: wrap;
} */
header {
  /* background-color: white; */
  line-height: 1.5;
  min-height: 5vh;
  max-height: 25vh;
  min-width: 100%;
  padding: 0 0 2rem 5rem;
  margin-bottom: 1rem;
  /* padding-bottom: 1rem; */
  display: flex;
  justify-content: space-between;
  /* border-bottom: 1px solid lightgray; */
  background-image: url(./assets/background5.png);
  background-repeat: no-repeat;
  background-size: cover;
}
.main-content-wrap {
  display: flex;
  flex-direction: row;
  min-height: 33vh;
}
.logo {
  display: block;
  margin: 0 auto 2rem;
}
nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
  margin-bottom: 1rem;
  text-transform: uppercase;
}
nav a {
  display: inline-block;
  padding: 0 1rem;
  font-weight: bold;
}
nav a.router-link-exact-active {
  color: var(--vt-c-indigo);
}
nav a.router-link-exact-active:hover {
  background-color: transparent;
}

.info-tools-wrap {
  display: flex;
  width: 100%;
  gap: 2rem;
  align-items: center;
}
@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }
}
.logo {
  margin: 0 2rem 0 0;
}

header .wrapper {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  width: 35vw;
}
nav {
  text-align: left;
  margin-left: -1rem;
  font-size: 1rem;
  display: flex;
  justify-content: space-between;
  padding: 1rem 0;
  margin-top: 1rem;
}
.basket-btn {
  width: 56px;
  height: 47px;
  border: 1px solid lightgray;
  border-radius: 3px;
  background-color: white;
  display: flex;
  /* justify-content: center; */
  padding-left: 7px;
  align-items: center;
}
.basket-btn:hover {
  background-color: lightgray;
  /* border-color: black; */
}
footer {
  width: 100%;
  height: 9rem;
  /* background-color: #3e454c; */
  display: flex;
  /* align-self: flex-end; */
  gap: 7px;
  padding: 3rem;
  align-items: center;
  background-image: url(./assets/background3.png);
  background-repeat: no-repeat;
}
/* h4 {
  font-style: italic;
} */
</style>
