# import sys
import os
import time
import random

import requests
import Adafruit_DHT

while True: 
    hum,temp=Adafruit_DHT.read_retry(11,4)
    payload = "field1={0:.3f}&field2={1:.3f}".format(temp, hum)
    try:
        print("making get request with params: {}".format(payload))
        requests.get("http://localhost:4000/api/v1/feed/push?{}".format(payload))
    except (keyboardInterrupt):
        break
    except Exception as e:
        print (e)
    time.sleep(5)

