import json
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt

# Store last 100 readings
temps = []
humidity = []
light = []
history = []

def on_message(client, userdata, msg):
    global temps, humidity, light, history
    # test if this work 
    data = json.loads(msg.payload.decode())
    print("Received:", data)

    # Store sensor values
    temps.append(data["temp"])
    humidity.append(data["humidity"])
    light.append(data["light"])

    # Keep only last 100 values
    if len(temps) > 100:
        temps.pop(0)
        humidity.pop(0)
        light.pop(0)

    # Save full data history
    history.append(data)
    if len(history) > 100:
        history.pop(0)

    with open("history.json", "w") as f:
        json.dump(history, f)

    # Update graphs
    plt.clf()

    plt.subplot(3, 1, 1)
    plt.title("Temperature")
    plt.plot(temps)

    plt.subplot(3, 1, 2)
    plt.title("Humidity")
    plt.plot(humidity)

    plt.subplot(3, 1, 3)
    plt.title("Light")
    plt.plot(light)

    plt.pause(0.1)


# MQTT setup
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

client.subscribe("iot/sensors")
client.on_message = on_message

# Enable live plotting
plt.ion()

print("Listening for data...")

client.loop_forever()
