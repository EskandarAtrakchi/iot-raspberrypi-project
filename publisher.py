import json
import time
import paho.mqtt.client as mqtt
from sensors import getTemp, getHumidity, getLight
from database import save_data

# Load config
with open("config.json") as f:
    config = json.load(f)

# MQTT setup
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

print("Starting publisher... Press CTRL+C to stop")

while True:
    temp = getTemp()
    humidity = getHumidity()
    light = getLight()

    data = {
        "device_id": config["device_id"],
        "latitude": config["latitude"],
        "longitude": config["longitude"],
        "temp": temp,
        "humidity": humidity,
        "light": light
    }

    # Send to cloud
    client.publish("iot/sensors", json.dumps(data))

    # Save locally
    save_data(temp, humidity, light)

    print("Sent:", data)

    time.sleep(5)
