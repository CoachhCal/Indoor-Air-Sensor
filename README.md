# Indoor Air Sensor


https://github.com/user-attachments/assets/2e4bec61-a309-4602-8b87-25747b6f36ea

## About
This project uses a Freenove ESP32-WROOM board and a BME680 sensor to gather indoor air data. The data is transmitted via a HiveMQ MQTT broker to a Flask backend, which stores it in a local MySQL database. The stored data is then displayed through a Vue.js frontend web application. 

## Technologies Used

- **ESP32 Microcontroller:** Freenove ESP32-WROOM
- **Sensor:** BME680 (Temperature, Humidity, Air Quality)
- **Communication Protocol:** MQTT via HiveMQ
- **Backend:** Flask (Python)
- **Database:** MySQL (accessed via SQLAlchemy)
- **Frontend:** Vue.js with TailwindCSS and Pinia for state management
- **Data Visualization:** Plotly.js

  
## ESP32 & BME680 Wiring

The tutorial used to set up the hardware: https://randomnerdtutorials.com/esp32-bme680-sensor-arduino/


![bme680-with-esp32-schematic-diagram-768x567](https://github.com/user-attachments/assets/b9ab9f79-7957-4161-861b-bd693789da7e)
