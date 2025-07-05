<script setup>
import RecentAirData from './components/RecentAirData.vue'
import Header from './components/Header.vue'

</script>

<template >
  <div class="page-wrapper">
    <Header/>
    <RecentAirData/>
  </div>
</template>

<style>
body {
  background-image: url('/forest.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  min-height: 100vh;
}

.page-wrapper {
  display: flex flex-column;
  justify-content: center; /* center horizontally */
  /* padding-top: 300px; */        /* push component down from top */
  min-height: 100vh;        /* ensure it takes full screen */
  box-sizing: border-box;
}
</style>
