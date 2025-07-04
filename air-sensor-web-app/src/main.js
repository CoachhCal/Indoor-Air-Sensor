import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faTemperatureHigh, faDroplet, faGauge, faTreeCity } from '@fortawesome/free-solid-svg-icons'

library.add(faTemperatureHigh, faDroplet, faGauge, faTreeCity)

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)

app.use(createPinia())

app.mount('#app')
