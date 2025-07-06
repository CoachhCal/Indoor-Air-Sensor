<script setup>

import { ref } from 'vue'
import latestSensorData from '../composables/latestSensorData'

const { timeCreated } = latestSensorData()

</script>

<template>

    <div class="header-container">

        <div class="flex gap-10  md:gap-20">
            <RouterLink to="/" class="nav-title">Home</RouterLink>
            <RouterLink to="/analytics" class="nav-title">Analytics</RouterLink>
        </div>
        <div class="flex justify-center text-center flex-row gap-x-5 mt-2 md:mt-0md:text-right md:ml-auto md:flex-col md:gap-x-0">
            <p class="text-yellow-500 text-xl md:text-md"> Last Updated </p> 
            <p class="nav-date"> {{timeCreated}}</p>
        </div>

    </div>

</template>

<style scoped>

.header-container {
    @apply flex items-center p-4 bg-black bg-opacity-70 w-full flex-col md:flex-row
}

.nav-title {
    @apply text-white text-3xl
}

.nav-date {
    @apply text-yellow-500 text-xl md:text-2xl
}

</style>
