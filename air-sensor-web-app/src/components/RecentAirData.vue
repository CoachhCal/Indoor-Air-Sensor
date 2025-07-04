<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const temperature = ref(null)
const humidity = ref(null)
const pressure = ref(null)
const gasResistance = ref(null)
const timeCreated = ref(null)
const rawDateCreated = ref(null)

const loading = ref(true)

const options = {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
}

onMounted(async () => {
    fetchRecentData()
    setInterval(fetchRecentData, 900000)
})

async function fetchRecentData() {
    try {
        const res = await axios.get('http://localhost:5000/api/sensors/latest')
        temperature.value = Math.round(res.data.temperature)
        humidity.value = Math.round(res.data.humidity)
        pressure.value = Math.round(res.data.pressure)
        gasResistance.value = Math.round(Number(res.data.gas_resistance))
        rawDateCreated.value = res.data.created_at
        timeCreated.value = new Date(rawDateCreated.value).toLocaleString('en-US', options);
        console.log(temperature.value)
    } catch (err) {
        console.error("Failed to load data")
    } finally {
        loading.value = false
    }
}



</script>


<template>
  <div class="grid grid-cols-1 max-w-[450px] md:grid-cols-2 md:h-[50vh] md:min-w-[300px] md:max-w-[650px] md:max-w-[1200px] 2xl:grid-cols-4 2xl:h-[25vh] 2xl:max-w-[1500px] mx-auto gap-4 p-5 border-4 border-green-900 bg-black bg-opacity-70 rounded-2xl">
    
    <div class="card">
        <p class="title">Temperature</p>
        <!-- temperature box -->
        <div class=" h-5/6 overflow-hidden">
            <!-- Picture and data -->
            <div class="results-container">
                <font-awesome-icon icon="temperature-high" text-white class="icon" />
                <p class="result">{{temperature}}&deg;C</p>
            </div>

            <div class="mt-1 h-2/3 overflow-auto justify-items-center">
                <p class="description" v-if="20 <= temperature && temperature <= 25"> Comfortable</p>
                <p class="description" v-else-if="temperature < 20"> Cool</p>
                <p class="description" v-else-if="temperature > 25"> Warm</p>
                <p class="description" v-else> N/A </p>
                <h3 class="p-2 mt-3 text-white text-center">Normal indoor air temperature ranges from 20&degC to 25&degC</h3>
                
            </div>
        </div>
    </div>

    <div class="card">
    
        <p class="title">Humidty</p>
        <!-- temperature box -->
        <div class=" h-5/6 overflow-hidden">
            <!-- Picture and data -->
            <div class="results-container">
                <font-awesome-icon icon="droplet" class="icon" />
                <p class="result">{{humidity}}%</p>
            </div>

            <div class=" mt-1 h-2/3 overflow-auto justify-items-center">
                <p class="description" v-if="40 <= humidity && humidity <= 60"> Comfortable</p>
                <p class="description" v-else-if="humidity < 40"> Dry</p>
                <p class="description" v-else-if="humidity > 25"> Humid</p>
                <p class="description" v-else> N/A </p>
                <h3 class="p-2 mt-3 text-white text-center">Optimal humidity is between 40% and 60%</h3>
                
            </div>
        </div>
    </div>

    <div class="card">
    
        <p class="title">Pressure</p>
        <!-- temperature box -->
        <div class=" h-5/6 overflow-hidden">
            <!-- Picture and data -->
            <div class="results-container">
                <font-awesome-icon icon="gauge" class="icon" />
                <p class="result">{{pressure}} hPa</p>
            </div>

            <div class=" mt-1 h-2/3 overflow-auto justify-items-center">
                <p class="description" v-if="(pressure - 1013) < 0"> {{1013 - pressure}} hPa below average </p>
                <p class="description" v-else-if="(pressure - 1013) > 0"> {{pressure - 1013}} hPa above average </p>
                <p class="description" v-else> Average</p>
                <h3 class="p-2 mt-3 text-white text-center">Average sea-level pressure in Halifax, NS is 1013 hPa</h3>
                
            </div>
        </div>
    </div>

    <div class="card">
    
        <p class="title">Gas Resistance</p>
        <!-- temperature box -->
        <div class=" h-5/6 overflow-hidden">
            <!-- Picture and data -->
            <div class="results-container">
                <font-awesome-icon icon="tree-city" class="icon" />
                <p class="result">{{gasResistance}} k&Omega;</p>
            </div>

            <div class=" mt-1 h-2/3 overflow-auto justify-items-center">
                <p class="description" v-if="gasResistance > 150"> Clean air </p>
                <p class="description" v-else-if="gasResistance < 50"> Polluted air </p>
                <p class="description" v-else> Average air quality</p>
                <h3 class="mt-5 text-white text-center">Polluted Air: 10k&Omega; - 49k&Omega; </h3>
                <h3 class="text-center text-white">Average Air: 51k&Omega; - 149k&Omega;</h3>
                <h3 class="text-center text-white">Clean Air: 150k&Omega;+ </h3>
                
            </div>
        </div>
    </div>

  </div>
</template>


<style scoped>
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
