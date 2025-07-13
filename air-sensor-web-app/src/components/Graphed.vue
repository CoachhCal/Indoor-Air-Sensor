<script setup>

import { ref, watch } from 'vue'
import Plotly from 'plotly.js-dist'
import allSensorData from '../composables/allSensorData'

const {
    temperatureArray,
    humidityArray,
    pressureArray,
    gasResistanceArray,
    timeStampsArray
} = allSensorData()

const selectedMetric = ref('temperature')

const metricLabels = {
    temperature: 'Temperature',
    humidity: 'Humidity',
    pressure: 'Pressure',
    gasResistance: 'Gas Resistance'
}

watch([selectedMetric, timeStampsArray], () => {

    const yData = {
        temperature: temperatureArray.value,
        humidity: humidityArray.value,
        pressure: pressureArray.value,
        gasResistance: gasResistanceArray.value
    }[selectedMetric.value]

    const trace = {
        type: 'scatter',
        mode: 'lines+markers',
        name: metricLabels[selectedMetric.value],
        x: timeStampsArray.value,
        y: yData,
        line: { color: '#17BECF'}
    }

    const layout = {
        title: metricLabels[selectedMetric.value] + ' Over Time',
        xaxis: {
            title: 'Time',
            type: 'date',
            rangeselector: {
                buttons: [
                    { count: 1, label: '1d', step: 'day', stepmode: 'backward' },
                    { count: 7, label: '1w', step: 'day', stepmode: 'backward' },
                    { step: 'all', label: 'All' }
                ]
            },
            rangeslider: {visible: true }
        },
        yaxis: {
            title: metricLabels[selectedMetric.value],
            autorange: true
        }
    }


    Plotly.newPlot('plotly-chart', [trace], layout)

})


</script>



<template>
  <div>
    <select v-model="selectedMetric">
      <option value="temperature">Temperature</option>
      <option value="humidity">Humidity</option>
      <option value="pressure">Pressure</option>
      <option value="gas_resistance">Gas Resistance</option>
    </select>

    <div id="plotly-chart"></div>
  </div>
</template>

