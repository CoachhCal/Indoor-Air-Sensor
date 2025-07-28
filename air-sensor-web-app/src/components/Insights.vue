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

    <div class="insight-wrapper">

        <div class="block">
            <p class="title"> Average {{metricStore.label}} </p>
            <p class="desc"> {{averageValue}} </p>
            
        </div>

        <div class="block">
            <p class="title"> Highest {{metricStore.label}} </p>
            <p class="desc"> {{minMaxValue.max}} </p>
            <p class="date"> {{minMaxValue.maxDate}} </p>
        </div>

        <div class="block">
            <p class="title"> Lowest {{metricStore.label}} </p>
            <p class="desc"> {{minMaxValue.min}} </p>
            <p class="date"> {{minMaxValue.minDate}} </p>
        </div>

    </div>

</template>



<style scoped>

.insight-wrapper {
    @apply flex justify-between min-h-[300px] pt-0 ps-5 pe-5 pb-5
}

.block {
    @apply flex flex-col w-1/3 m-2 border-2 border-blue-500 text-white items-center
}

.title {
    @apply text-2xl m-2
}

.desc {
    @apply text-4xl m-2
}

.date {
    @apply text-xl m-2
}

</style>