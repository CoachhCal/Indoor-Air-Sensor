<script setup>

import {ref, watch, computed, onMounted, onUnmounted } from 'vue'
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

const isXL = ref(window.innerWidth >= 1280)

const updateScreenSize = () => {
  isXL.value = window.innerWidth >= 1280
}

onMounted(() => {
  window.addEventListener('resize', updateScreenSize)
})

onUnmounted(() => {
  window.removeEventListener('resize', updateScreenSize)
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

    <div v-if="isXL" class="insight-wrapper">

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

    <div v-else class="insight-wrapper">

        <div class="block">
            <div>
                <p class="title"> Average {{metricStore.label}} </p>
                <p class="date">{{firstRecord}} - {{lastRecord}}</p>
            </div>
            <div>
                <p class="desc"> {{averageValue}}{{metricStore.unit}} </p>
            </div>
            
        </div>

        <div class="block">
            <div>
                <p class="title"> Highest {{metricStore.label}} </p>
                <p class="date"> {{minMaxValue.maxDate}} </p>
            </div>
            <div>
                <p class="desc"> {{minMaxValue.max}}{{metricStore.unit}} </p>
            </div>
            
        </div>

        <div class="block">
            <div>
                <p class="title"> Lowest {{metricStore.label}} </p>
                <p class="date"> {{minMaxValue.minDate}} </p>
            </div>
            <div>
                <p class="desc"> {{minMaxValue.min}}{{metricStore.unit}} </p>
            </div>
            
        </div>

    </div>

</template>



<style scoped>

.insight-wrapper {
    @apply flex items-center xl:flex-row xl:justify-between xl:p-5 overflow-x-auto overflow-y-hidden;
}

.block {
    @apply flex flex-col flex-shrink-0 w-[300px] m-2 mb-5 rounded-2xl text-white items-center 
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