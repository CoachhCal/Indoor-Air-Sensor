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
 
const options = {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    };

    const optionsShort = {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
    };

const dateArr = computed(() => timeStampsArray.value)

const firstRecord = computed(() => {
  const arr = dateArr.value
  if (!arr) return 'N/A'
  return new Date(arr[0]).toLocaleString('en-US', optionsShort)
})

const lastRecord = computed(() => {
  const arr = dateArr.value
  if (!arr) return 'N/A'
  return new Date(arr[arr.length - 1]).toLocaleString('en-US', optionsShort)
})

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

    const arr = metricArray.value

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
    let minDate = dateArr.value[0]
    let maxDate = dateArr.value[0]

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
            <p class="desc"> {{averageValue}}{{metricStore.unit}} </p>
            <p class="date">{{firstRecord}} - {{lastRecord}}</p>
            
            
        </div>

        <div class="block">
            <p class="title"> Highest {{metricStore.label}} </p>
            <p class="desc"> {{minMaxValue.max}}{{metricStore.unit}} </p>
            <p class="date"> {{minMaxValue.maxDate}} </p>
        </div>

        <div class="block">
            <p class="title"> Lowest {{metricStore.label}} </p>
            <p class="desc"> {{minMaxValue.min}}{{metricStore.unit}} </p>
            <p class="date"> {{minMaxValue.minDate}} </p>
        </div>

    </div>

</template>



<style scoped>

.insight-wrapper {
    @apply flex justify-between pt-5 ps-5 pe-5 pb-5
}

.block {
    @apply flex flex-col w-1/3 m-2 rounded-2xl text-white items-center 
}

.title {
    @apply text-2xl m-2
}

.desc {
    @apply text-4xl m-2
}

.date {
    @apply text-xl m-2 mt-5
}

</style>