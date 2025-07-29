import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useMetricStore = defineStore('selectedMetric', () => {

  const metric = ref('temperature')

  const label = computed(() => {

    const labels = {
        temperature: 'Temperature',
        humidity: 'Humidity',
        pressure: 'Pressure',
        gasResistance: 'Gas Resistance'
    }

    return labels[metric.value] || 'None'
    
  })

  const unit = computed(() => {

    const units = {
        temperature: '°C',
        humidity: '%',
        pressure: 'hPa',
        gasResistance: 'kΩ'
    }

    return units[metric.value] || 'None'
    
  })

  function setMetric(newMetric) {
    metric.value = newMetric
  }

  return { metric, label, unit, setMetric }
})
