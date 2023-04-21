import tkinter as tk
import random
import requests
import json

urlEndpoint = "http://localhost:4000/api/v1"

def sendAction():
    payload = "field1={0:.3f}&field2={1:.3f}".format(26 + 1.2 * random.random(),89 + 1.2 * random.random())
    requests.get("{}/feed/push?{}".format(urlEndpoint, payload))

    fetchAction()

def fetchAction():
    out = requests.get("{}/feed".format(urlEndpoint))
    data = json.loads(out.text)
    text = ""

    for i, record in enumerate(data):
        text += "{}, {}, {}\n".format(record['entry_id'], record['temp'], record['hum'])

    dataPres = tk.Label(window, text=text, font=("Arial", 14))
    dataPres.grid(row=4, column=0)


if __name__ == "__main__":
    window = tk.Tk()
    greeting = tk.Label(window, text="Hello, Tkinter", font=("Arial", 20))
    greeting.grid(row=0, column=0)

    send = tk.Button(window, text="send sensor data", font=("Arial", 16), command=sendAction)
    send.grid(row=1, column=0)

    fetch = tk.Button(window, text="Fetch sensor data from DB", font=("Arial", 16), command=fetchAction)
    fetch.grid(row=2, column=0)


    fetchAction()

    window.mainloop()
