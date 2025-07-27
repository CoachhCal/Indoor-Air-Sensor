<script setup>

import { useMetricStore } from '@/stores/selectedMetric'

const metricStore = useMetricStore()

function onSelectChange(e) {
    console.log(e.target.value)
    metricStore.setMetric(e.target.value)
}

</script>

<template>

    <div class="container">

        <button @click="onSelectChange" value="temperature" class="metrics">Temperature</button>
        <button @click="onSelectChange" value="humidity" class="metrics">Humidity</button>
        <button @click="onSelectChange" value="pressure" class="metrics">Pressure</button>
        <button @click="onSelectChange" value="gasResistance" class="metrics">Gas Resistance</button>

    </div>

</template>

<style scoped>

.container {
    @apply ms-2 me-2 mt-0 flex flex-col justify-evenly mx-auto gap-4 p-5 border-4 border-green-900 bg-black bg-opacity-70 rounded-2xl
}

.metrics {
    @apply text-white text-2xl
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