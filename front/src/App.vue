<script setup>
import { RouterLink, RouterView } from "vue-router";
import PhoneNumbers from "./components/PhoneNumbers.vue";
import MenuViewVue from "./views/MenuView.vue";
import SearchInput from "./components/SearchInput.vue";
</script>

<template>
  <div>
    <header>
      <RouterLink to="/"
        ><img
          alt="Vue logo"
          class="logo"
          src="./assets/logo22.jpg"
          width="208"
          height="89"
      /></RouterLink>

      <div class="header-menu-wrap">
        <nav>
          <RouterLink to="/">Головна</RouterLink>
          <RouterLink to="/payment">Оплата</RouterLink>
          <RouterLink to="/delivery">Доставка</RouterLink>
          <RouterLink to="/guarantee">Гарантія</RouterLink>
        </nav>
        <div class="info-tools-wrap">
          <PhoneNumbers class="phone" msg="(093)111-22-33, (067)123-45-67" />
          <SearchInput />
          <RouterLink to="/basket">
            <div class="basket-btn">
              <img
                src="./assets/basket.png"
                alt=""
                width="35px"
                height="30px"
              />
            </div>
          </RouterLink>
        </div>
      </div>
    </header>
    <div class="main-content-wrap">
      <MenuViewVue />
      <RouterView />
    </div>
    <footer class="footer">
      <img src="./assets/Copy2.png" alt="" width="13px" height="13px" />
      <h4>Created by Medvediev & Kolesnyk - 2024</h4>
    </footer>
  </div>
</template>

<style>
header {
  /* background-color: white; */
  line-height: 1.5;
  min-height: 5vh;
  max-height: 25vh;
  min-width: 100vw;
  padding: 0 0 2rem 5rem;
  margin-bottom: 1rem;
  display: flex;
  /* justify-content: space-between; */
  gap: 43%;
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
  .logo {
    margin: 1rem 2rem 0 0.3rem;
  }
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
}
@media (max-width: 1540px) {
  .main-content-wrap {
    width: 100vw;
    flex-direction: row-reverse;
    flex-wrap: wrap;
    flex-direction: column-reverse;
    justify-content: space-around;
    align-items: self-start;
    gap: 10rem;
    padding-left: 1rem;
  }
  /* .goods-page-wrap {
    min-width: 80%;
    gap: 10rem;
  } */
  .phone {
    font-size: 12px;
  }
}
@media (max-width: 1490px) {
  /* .goods-page-wrap {
    justify-content: space-around;
    width: 90%;
    gap: 20rem;
  } */
  header {
    gap: 30%;
  }
  .phone {
    font-size: 9px;
  }
}
@media (max-width: 1090px) {
  .main-content-wrap {
    justify-content: flex-end;
    flex-direction: row-reverse;
    flex-wrap: wrap;
    gap: 18rem;
  }
  header {
    gap: 15%;
    margin: 0 0 1rem;
  }

  /* .goods-page-wrap {
    flex-direction: column;
  } */
  .banner {
    display: none;
  }
}
@media (max-width: 1024px) {
  .main-content-wrap {
    min-width: 100%;
    gap: 2rem;
    margin: 0 auto;
  }
  header {
    min-width: 99%;
    min-height: 14rem;
    padding: 0 0 2rem 2rem;
    gap: 2%;
    flex-wrap: wrap;
    margin-bottom: 4rem;
  }
}
@media (max-width: 1090px) {
  .header-menu-wrap {
    gap: 0.1rem;
  }
  .logo {
    margin: 1rem 1rem 0 0.3rem;
  }
}
@media (max-width: 650px) {
  nav {
    max-width: 10rem;
  }
  .nav,
  a {
    gap: 0.5rem;
    font-size: 11px;
    justify-content: space-around;
  }
  .info-tools-wrap {
    flex-wrap: wrap;
    gap: 1.5rem;
  }
  .info-tools-wrap label {
    width: 8rem;
    height: 1.5rem;
  }

  header {
    position: relative;
    /* background-size: cover; */
  }
  .basket-btn {
    position: absolute;
    top: 2rem;
    right: 2rem;
  }
  .main-content-wrap aside {
    margin: 0;
    max-width: 20rem;
    border: none;
  }
  .main-content-wrap .goods-page-wrap {
    flex-wrap: wrap;
    gap: 5rem;
  }
  .main-content-wrap .item-cart {
    min-width: 17rem;
  }
  .main-content-wrap .wrap {
    padding-left: 1rem;
  }
}

.footer {
  min-width: 100%;
  min-height: 17rem;
  /* background-color: #3e454c; */
  display: flex;
  /* align-self: flex-end; */
  gap: 7px;
  padding: 4rem;
  align-items: end;
  background-image: url(./assets/background3.png);
  background-repeat: no-repeat;

  /* place-self: end; */
}
</style>
