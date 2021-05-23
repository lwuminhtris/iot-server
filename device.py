import random
import time
from Adafruit_IO import Client, MQTTClient

"""
aio = Client("mitapari", "aio_kwOZ52nJ4Yp4sU9YdMlTnCeSIzoO")

# Send the value 100 to a feed called 'Foo'.
aio.send("test", "OFF")

# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
data = aio.receive("test")
print("Received value: {0}".format(data.value))
"""

aio = Client("mitapari", "aio_LyIt57jRbeBfHM4EJ7YDpd2MOq5C")


def connected(mqttClient):
    print("Connected to client ..")
    mqttClient.subscribe("test")


def disconnected(mqttClient):
    # Disconnected function will be called when the client disconnects.
    print("Disconnected from Adafruit IO!")


def message(mqttClient, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print("Feed {0} received new value: {1}".format(feed_id, payload))


mqttClient = MQTTClient("mitapari", "aio_LyIt57jRbeBfHM4EJ7YDpd2MOq5C")

mqttClient.on_connect = connected
mqttClient.on_disconnect = disconnected
mqttClient.on_message = message

mqttClient.connect()

mqttClient.loop_background()


def feedOn():
    param = "ON"
    mqttClient.publish("test", param)
    print("Publishing {} to sensor".format(param))
    return {"status": "OK", "description": param}


def feedOff():
    param = "OFF"
    mqttClient.publish("test", param)
    print("Publishing {} to sensor".format(param))
    return {"status": "OK", "description": param}


def latestDataRetrieve():
    data = aio.receive(feed="test")
    return {"value": data.value}


def allDataRetrieve():
    data = data = aio.receive(feed="test")
    return data
