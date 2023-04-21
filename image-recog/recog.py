import sys

import numpy as np
import matplotlib.pyplot as plt
import cv2
import tflite_runtime.interpreter as tflite

model_path = "./models/mobilenet_v1_1.0_224_quant.tflite"
labels_path = "./models/labels_mobilenet_quant_v1_224.txt"

def predictImage(img_path, interpreter):
    inp_details = interpreter.get_input_details()
    out_details = interpreter.get_output_details()

    w = inp_details[0]['shape'][1]
    h = inp_details[0]['shape'][2]

    # CV2 loads the color channel in BGR order
    # changing the order to RGB
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # resizing the image according to the model input
    img = cv2.resize(img, (w,h))
    plt.imshow(img)

    input = np.expand_dims(img, axis=0)

    # classify the given input by passing into the model interpreter
    interpreter.set_tensor(inp_details[0]['index'], input)
    interpreter.invoke()

    # return the predictions for 1001 classes
    return interpreter.get_tensor(out_details[0]['index'])[0]

def filterNPredictions(predictions, labels, n):
    # the ::-1 is used to reverse array
    # the :n is used to get the first n values from the array
    top_n_results = np.argsort(predictions)[::-1][:n]

    # printing all the results obtained
    for i in top_n_results:
        print(labels[i], predictions[i]/255.0)

if __name__ == "__main__":
    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    labels = {}

    with open(labels_path, 'r') as lbl_file:
        labels = {idx:label.strip() for idx, label in enumerate(lbl_file.readlines())}

    img_path = sys.argv[1]

    predictions = predictImage(img_path, interpreter)
    filterNPredictions(predictions, labels, 5)
