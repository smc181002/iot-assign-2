# import sys
import os
import time
import random

import Adafruit_DHT
import paho.mqtt.publish as publish
from dotenv import load_dotenv

load_dotenv()

username= os.environ['username']
clientID=os.environ['clientId']
password=os.environ['password']

channelID = "2088972"

mqtt_host = "mqtt3.thingspeak.com"

topic = "channels/{}/publish".format(channelID)
t_transport = "websockets"
t_port = 80

while True: 
    hum,temp=Adafruit_DHT.read_retry(11,4)
    # payload = "field1={0:.3f}&field2={1:.3f}".format(26 + 1.2 * random.random(),89 + 1.2 * random.random())
    payload = "field1={0:.3f}&field2={1:.3f}".format(temp, hum)
    try:
        print("writing payload: {}".format(payload))
        publish.single(
            topic, 
            payload, 
            hostname=mqtt_host, 
            transport=t_transport, 
            port=t_port, 
            client_id=clientID, 
            auth={'username':username,'password':password}
        )
    except (keyboardInterrupt):
        break
    except Exception as e:
        print (e)
    time.sleep(5)

