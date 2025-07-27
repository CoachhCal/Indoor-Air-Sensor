<script setup>

import { ref, watch } from 'vue'
import Plotly from 'plotly.js-dist'
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

watch([ () => metricStore.metric, timeStampsArray], () => {


    const yData = {
        temperature: temperatureArray.value,
        humidity: humidityArray.value,
        pressure: pressureArray.value,
        gasResistance: gasResistanceArray.value
    }[metricStore.metric]

    const trace = {
        type: 'scatter',
        mode: 'lines+markers',
        name: metricStore.label,
        x: timeStampsArray.value,
        y: yData,
        line: { color: '#17BECF'}
    }

    const layout = {
        title: {text: metricStore.label + ' Over Time'},
        xaxis: {
            title: {text: 'Time'},
            type: 'date',
            range: [timeStampsArray.value[0], timeStampsArray.value[timeStampsArray.value.length - 1]],
            autorange: false,
            rangeselector: {
                buttons: [
                    { count: 1, label: '1d', step: 'day', stepmode: 'backward' },
                    { count: 7, label: '1w', step: 'day', stepmode: 'backward' },
                    { step: 'all', label: 'All' }
                ]
            },
            
        },
        yaxis: {
            title: { text: metricStore.label},
            autorange: true
        }
    }

    if (!timeStampsArray.value || !timeStampsArray.value.length || !yData?.length) {
        return; // Skip plotting if data isn't ready
    }



    Plotly.newPlot('plotly-chart', [trace], layout)

})




</script>



<template>
  <div id="plotly-chart" class="w-full h-full"></div>
</template>

<style scoped>
    #plotly-chart {
    width: 100%;
    height: 100%;
    }
</style>

