# Working with Raspberry PIs

1. Build GUI application to Implementing the MQTT subscribe
operation to the given demo MQTT publish operation using Thingspeak
Cloud.

2. Develop a Restful API application to collect, store the DHT sensor data
and run the application on a RPi.

3. Develop a Python GUI application to collect and store sensor data locally
in the MySQL DB. Connect to Raspberry Pi+DHT11 Sensor.

4. Develop a program to perform image classification task by capturing the
images using RPi using Tensorflowlite.

## Question 1

The publisher is written in python and can be found at [mqtt-publish](./mqtt-publish)
directory in this repository

Enter this directory and to install the required packages, press the below command

```bash
pip3 install -r requirements.txt
```

Create a `.env` directory and enter the following values to publish to the cloud:

```env
username=<enter_username_here>
clientId=<enter_clientId_here>
password=<enter_password_here>
```

Then run `python3 publish.py` to run the publisher code to push to thingspeak

The [GUI Application](./gui-mqtt-sub-tauri) is built using Tauri that 
uses Javascript and Rust.

Requirements:

1. Install Node.js
2. Install Rust

Read the prerequisites to setup the environment locally
https://tauri.app/v1/guides/getting-started/prerequisites

Once environment is setup, clone this repository and enter the `gui-mqtt-sub-tauri`
directory and press the below commands

```bash
yarn install
yarn tauri dev
```

If yarn is not installed, use the below command to install
```bash
npm install -g yarn
```

## Question 2

The REST API is built using express-ts from a template I have put up at 
[ceoldevs/express-ts-minimal](https://github.com/ceoldevs/express-ts-minimal)
and sequelize ORM to connect to the database(mariadb)

The code is available at - [rest-api-mysql](./rest-api-mysql)

The client code to collect DHT sensor data is located at - [restclient](./restclient)

## Question 3

The 3rd questions uses Tkinter as the GUI which acts as client to push the data to REST API
developed in question 2.

location for the gui code is - [python-gui](./python-gui)

## Question 4

The code is located at - [image-recog](./image-recog)

The directory for model and it's lables should be located at in the `models` directory and named as:
* model_path = `"./models/mobilenet_v1_1.0_224_quant.tflite"`
* labels_path = `"./models/labels_mobilenet_quant_v1_224.txt"`
