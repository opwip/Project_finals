<script setup></script>

<template>
  <div class="wrap">
    <h1>Дякуємо! Ваше замовлення прийняте</h1>
    <br />
    <h4>Наразі воно обробляється, очікуйте листа на вказаий Вами Email</h4>
    <RouterLink to="/"> <button class="finalBtn">Далі</button></RouterLink>
  </div>
</template>

<style scoped>
.wrap {
  width: 30vw;
  position: relative;
}
h4 {
  font-weight: bold;
  font-style: italic;
}
.finalBtn {
  width: 70px;
  height: 25px;
  position: absolute;
  right: 3rem;
  top: 19rem;
}
</style>
