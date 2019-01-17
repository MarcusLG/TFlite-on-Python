# TFlite-on-Python
Running inference using TensorFlow Lite .tflite and .lite model on Python, for model trouble-shooting before deployment to mobile platform.

## Overview
The programme creates a TFlite interpreter in the Python environment which supports inteferences to be run to test the accuracy of the 
converted TFlite model either from a frozen .pb file or a Keras .h5 file. Batch input is will be supported by concatenating the input, 
x_matrix with multiple input_matrix.

## Setup needed:
The model path shall be added to the variable path_1, after which the programme can be run with:
```
python3 main.py
```
The output shall be presented in the form:
```
[[1., 0., 0., 0.]]
```
## Run with Notebook
Link:
https://colab.research.google.com/drive/1MgaAoPSdXiQRKpQZMCwpRapTNytwINcX
