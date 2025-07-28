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
        title: {
            text: metricStore.label + ' Over Time',
            font: {
                size: 26
            }
        },
        xaxis: {
            title: {
                text: 'Time',
                font: {
                    size: 22
                }
            },
            type: 'date',
            range: [timeStampsArray.value[0], timeStampsArray.value[timeStampsArray.value.length - 1]],
            autorange: false,
            rangeselector: {
                buttons: [
                    { count: 1, label: '1d', step: 'day', stepmode: 'backward' },
                    { count: 7, label: '1w', step: 'day', stepmode: 'backward' },
                    { step: 'all', label: 'All' }
                ],
                bgcolor: '#444',        
                activecolor: '#1A7300',
            },
            showgrid:true,
            gridcolor: '#1C1C1C',
            zeroline: true,
            zerolinecolor: '#ffffff',
            linecolor: '#aaa',
            tickcolor: '#aaa'
            
        },
        yaxis: {
            title: {
                text: metricStore.label,
                font: {
                    size: 22
                }
            },
            autorange: true,
            showgrid:true,
            gridcolor: '#1C1C1C',
            zeroline: true,
            zerolinecolor: '#ffffff',
            linecolor: '#aaa',
            tickcolor: '#aaa'
        },
        plot_bgcolor: '#000000',
        paper_bgcolor: '#000000',
        font: {
            color: 'white',
        },
        margin: {
            l: 100,
            b: 100,
        }
        
        
    }

    const config = {
        responsive: true,
        useResizeHandler: true
    }

    if (!timeStampsArray.value || !timeStampsArray.value.length || !yData?.length) {
        return; // Skip plotting if data isn't ready
    }



    Plotly.newPlot('plotly-chart', [trace], layout, config)

})




</script>



<template>
  <div class="container">

    <div id="plotly-chart" class="chart-inner"></div>
  
  </div>
</template>

<style scoped>

    #plotly-chart {
        width: 100%;
        height: 100%;
    }

    .container {
        @apply flex w-full h-full p-5
    }

    .chart-inner {
        width: 100%;
        height: 100%;
}

</style>

