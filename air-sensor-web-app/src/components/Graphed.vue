<script setup>

import { ref } from 'vue'
import allSensorData from '../composables/allSensorData'

const {
    temperatureArray,
    humidityArray,
    pressureArray,
    gasResistanceArray,
    timeStampsArray
} = allSensorData()

</script>



<template>

</template>

