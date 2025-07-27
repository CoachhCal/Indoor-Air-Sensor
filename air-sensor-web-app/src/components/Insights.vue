<script setup>

import {ref, watch, computed } from 'vue'
import allSensorData from '../composables/allSensorData'
import { useMetricStore } from '@/stores/selectedMetric'

const {
    temperatureArray,
    humidityArray,
    pressureArray,
    gasResistanceArray,
    timeStampsArray
} = allSensorData()

const metricStore = useMetricStore()

const metricArray = computed (() => ({
    temperature: temperatureArray.value,
    humidity: humidityArray.value,
    pressure: pressureArray.value,
    gasResistance: gasResistanceArray.value
}[metricStore.metric] ?? []))

const averageValue = computed(() => {
    const arr = metricArray.value

    if (!Array.isArray(arr) || arr.length === 0) {
        return 0;
    }

    const arrLength = arr.length

    const arrSum = arr.reduce((acc, curr) => acc + curr, 0);
    const average = arrLength === 0 ? 0 : arrSum / arrLength

    return Math.round(average);
});

const minMaxValue = computed(() => {

    const options = {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    };

    const arr = metricArray.value
    const dateArr = timeStampsArray

    if (!arr.length) {
        return {
            min: 0,
            max: 0,
            minDate: 'N/A',
            maxDate: 'N/A'
        };
    }

    let max = arr[0];
    let min = arr[0];
    let minDate = dateArr[0]
    let maxDate = dateArr[0]

    for (let i = 1; i < arr.length; i++){
        if (arr[i] > max){
            max = arr[i];
            maxDate = dateArr.value[i];
        }
        if (arr[i] < min){
            min = arr[i];
            minDate = dateArr.value[i]
        }
    }

    return {
        min: Math.round(min),
        minDate: new Date(minDate).toLocaleString('en-US', options),
        max: Math.round(max),
        maxDate: new Date(maxDate).toLocaleString('en-US', options),
    };
})

</script>



<template>

    <div class="container">

        <div class="block">
            <p> Average {{metricStore.label}} </p>
            <p> {{averageValue}} </p>
            
        </div>

        <div class="block">
            <p> Maximum {{metricStore.label}} </p>
            <p> {{minMaxValue.max}} </p>
            <p> {{minMaxValue.maxDate}} </p>
        </div>

        <div class="block">
            <p> Minimum {{metricStore.label}} </p>
            <p> {{minMaxValue.min}} </p>
            <p> {{minMaxValue.minDate}} </p>
        </div>

    </div>

</template>



<style scoped>

.container {
    @apply flex justify-between p-5 border-2 border-red-500
}

.block {
    @apply flex flex-col w-1/3 m-2 border-2 border-blue-500 text-white items-center
}

</style>