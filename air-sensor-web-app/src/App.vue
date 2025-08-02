<script setup>
import RecentAirData from './components/RecentAirData.vue'
import Header from './components/Header.vue'

</script>

<template >
  <div class="page-wrapper">
    <Header/>
    <router-view/>
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
  justify-content: center;
  min-height: 100vh;        
  box-sizing: border-box;
}
</style>
