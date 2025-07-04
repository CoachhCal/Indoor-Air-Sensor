from flask import Flask, jsonify
from flask_cors import CORS
from routes import insert_sensor_data, retrieve_recent_data
import paho.mqtt.client as mqtt
import json
from dotenv import load_dotenv
import os


app = Flask(__name__)
CORS(app)

load_dotenv()

latest_payload = {
    "temperature":None,
    "humidity":None,
    "pressure":None,
    "gas_resistance":None
    }

@app.route("/api/sensors/latest", methods=["GET"])
def get_recent_sensor_data():
    data = retrieve_recent_data()
    if "error" in data or "message" in data:
        return jsonify(data), 404
    return jsonify(data), 200

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("sensor/apart")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"Recieved MQTT message: {payload}")

    try:

        data = json.loads(payload)

        latest_payload["temperature"] = float(data["temp"]) - 4
        latest_payload["humidity"] = float(data["humidity"])
        latest_payload["pressure"] = float(data["pressure"])
        latest_payload["gas_resistance"] = float(data["gas"])


        insert_sensor_data(
            latest_payload["temperature"],
            latest_payload["humidity"],
            latest_payload["pressure"],
            latest_payload["gas_resistance"]
        )

    except Exception as e:
        print(f"Error: {e}")


mqtt_client = mqtt.Client()

mqtt_client.tls_set()
mqtt_client.username_pw_set(os.getenv("MQTT_USERNAME"), os.getenv("MQTT_PASSWORD"))

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(os.getenv("MQTT_URL"), 8883, 60)
mqtt_client.loop_start()



if __name__ == '__main__':
    app.run(debug=True)

#flask run