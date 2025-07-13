import { ref, onMounted} from 'vue'
import axios from 'axios'

const temperatureArray = ref(null)
const humidityArray = ref(null)
const pressureArray = ref(null)
const gasResistanceArray = ref(null)
const timeStampsArray = ref(null)

async function fetchAllData() {
    try{
        const res = await axios.get('http://localhost:5000/api/sensors/all-data')
        timeStampsArray.value = res.data.timestamps
        temperatureArray.value = res.data.temperature
        humidityArray.value = res.data.humidity
        pressureArray.value = res.data.pressure
        gasResistanceArray.value = res.data.gas_resistance
    } catch (err) {
        console.error("Failed to load all sensor data")
    }

}

function allSensorData() {
  onMounted(() => {
    fetchAllData()
    setInterval(fetchAllData, 900000) // 15 min refresh
  })

  return {
    temperatureArray,
    humidityArray,
    pressureArray,
    gasResistanceArray,
    timeStampsArray
  }

}

export default allSensorData