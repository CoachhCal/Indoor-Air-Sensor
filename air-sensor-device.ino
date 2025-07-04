#include <PubSubClient.h>
#include <Zanshin_BME680.h>
#include <Wire.h>
#include <WiFi.h>
#include <WiFiClientSecure.h>

const char* SSID = "";
const char* PASSWORD = "";

unsigned long previousMillis = 0;
unsigned long wifiReconnectInterval = 30000;
unsigned long lastSendTime = 0;
const unsigned long sendInterval = 1800000; // Publish data every 30 minutes

const char* mqtt_server = "";
const int mqtt_port = ;
const char* mqtt_user = "";
const char* mqtt_pass = "";
const char* topic = "";

WiFiClientSecure espClient;
PubSubClient client(espClient);
BME680_Class bme;  // Create instance of the sensor class

void initWiFi() {

  WiFi.mode(WIFI_STA);
  WiFi.begin(SSID, PASSWORD);
  Serial.print("Connecting to WiFi ..");

  while(WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(1000);
  }

  Serial.println(WiFi.localIP());

}

void connectMQTT() {

  espClient.setInsecure();
  client.setServer(mqtt_server, mqtt_port);

  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ESP32Client", mqtt_user, mqtt_pass)) {
      Serial.println("✅ Connected");
    } else {
      Serial.print("❌ Failed, rc=");
      Serial.print(client.state());
      Serial.println(" trying again...");
      delay(3000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  Wire.begin();

  // Initialize the sensor
  if (!bme.begin()) {
    Serial.println("BME680 sensor not found. Check wiring.");
    while (true);  // Stop here if no sensor found
  }

  // Set oversampling rates
  bme.setOversampling(TemperatureSensor, Oversample8);
  bme.setOversampling(HumiditySensor, Oversample2);
  bme.setOversampling(PressureSensor, Oversample4);
  bme.setIIRFilter(IIR4);               
  bme.setGas(320, 150);                 

  initWiFi();
  connectMQTT();

}

void loop() {

  unsigned long currentMillis = millis();
    // if WiFi is down, try reconnecting every CHECK_WIFI_TIME seconds
  if ((WiFi.status() != WL_CONNECTED) && (currentMillis - previousMillis >=wifiReconnectInterval)) {
    Serial.print(millis());
    Serial.println("Reconnecting to WiFi...");
    WiFi.disconnect();
    WiFi.reconnect();
    previousMillis = currentMillis;
  }

  if (!client.connected()) {
  connectMQTT();
  }
  client.loop();


  // Trigger a measurement and wait for it to finish
  bme.triggerMeasurement();
  while (bme.measuring()) {
    delay(10);
  }

  int32_t temp, hum, pres, gas;
  bme.getSensorData(temp, hum, pres, gas);

  // Convert to float values for display
  float temperature = temp / 100.0;
  float humidity    = hum / 1000.0;
  float pressure    = pres / 100.0;
  float gasKOhms    = gas / 1000.0;

  String payload = "{";
  payload += "\"temp\":" + String(temperature, 2) + ",";
  payload += "\"humidity\":" + String(humidity, 2) + ",";
  payload += "\"pressure\":" + String(pressure, 2) + ",";
  payload += "\"gas\":" + String(gasKOhms, 2);
  payload += "}";


  if (currentMillis - lastSendTime >= sendInterval) {
    Serial.println("Publishing: " + payload);
    client.publish(topic, payload.c_str());
    lastSendTime = currentMillis;
  }

  delay(5000);  // Wait before next reading
}
