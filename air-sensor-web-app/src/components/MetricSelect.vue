<script setup>

import { useMetricStore } from '@/stores/selectedMetric'
import { computed } from 'vue'

const metricStore = useMetricStore()

const selectedMetric = computed(() => metricStore.metric)

//Changes the metric value which updates the graph with the relevant information
function onSelectChange(e) {
    metricStore.setMetric(e.target.value)
}

</script>

<template>

    <div class="metric-container">

        <button
            @click="onSelectChange"
            value="temperature"
            class="metrics"
            :class="metricStore.metric === 'temperature' ? 'text-yellow-500' : 'text-white'"
        >Temperature</button>

        <button
            @click="onSelectChange"
            value="humidity" 
            class="metrics"
            :class="selectedMetric === 'humidity' ? 'text-yellow-500' : 'text-white'"
        >Humidity</button>

        <button
            @click="onSelectChange"
            value="pressure"
            class="metrics"
            :class="selectedMetric === 'pressure' ? 'text-yellow-500' : 'text-white'"
        >Pressure</button>

        <button
            @click="onSelectChange"
            value="gasResistance"
            class="metrics"
            :class="selectedMetric === 'gasResistance' ? 'text-yellow-500' : 'text-white'"
        >Gas Resistance</button>

    </div>

</template>

<style scoped>

.metric-container {
    @apply m-0 flex flex-row justify-evenly mx-auto gap-4 p-5 border-4 border-green-900 bg-black w-full bg-opacity-70 rounded-2xl xl:flex-col xl:ms-2 xl:me-2 mt-0 
}

.metrics {
    @apply text-2xl
}

.card {
    @apply rounded-2xl p-2 h-full min-w-[300px]
}

.title {
    @apply text-2xl mb-2 text-white justify-self-center
}

.results-container {
    @apply flex items-center justify-evenly h-1/3 p-5
}

.icon {
    @apply text-5xl text-white
}

.result {
    @apply text-4xl text-white
}

.description {
    @apply text-lg text-white
}

</style>