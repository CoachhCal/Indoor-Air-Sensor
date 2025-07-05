import { ref, onMounted } from 'vue'
import axios from 'axios'

const temperature = ref(null)
const humidity = ref(null)
const pressure = ref(null)
const gasResistance = ref(null)
const rawDateCreated = ref(null)
const timeCreated = ref(null)
const loading = ref(true)

const options = {
  dateStyle: 'short',
  timeStyle: 'short'
}

async function fetchRecentData() {
  try {
    const res = await axios.get('http://localhost:5000/api/sensors/latest')
    temperature.value = Math.round(res.data.temperature)
    humidity.value = Math.round(res.data.humidity)
    pressure.value = Math.round(res.data.pressure)
    gasResistance.value = Math.round(Number(res.data.gas_resistance))
    rawDateCreated.value = res.data.created_at
    timeCreated.value = new Date(rawDateCreated.value).toLocaleString('en-US', options)
  } catch (err) {
    console.error("Failed to load data")
  } finally {
    loading.value = false
  }
}

function latestSensorData() {
  onMounted(() => {
    fetchRecentData()
    setInterval(fetchRecentData, 900000) // 15 min refresh
  })

  return {
    temperature,
    humidity,
    pressure,
    gasResistance,
    rawDateCreated,
    timeCreated,
    loading
  }
}

export default latestSensorData