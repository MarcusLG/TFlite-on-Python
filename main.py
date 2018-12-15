import tensorflow as tf
import tkinter as tk
from tkinter import filedialog
import PIL
from PIL import Image
import numpy as np


# DEF. PARAMETERS
img_row, img_column = 200, 200
num_channel = 1
num_batch = 1
# include the path containing the model (.lite, .tflite)
path_1 = r""


# TFLITE INTERPRETER CON.
interpreter = tf.contrib.lite.Interpreter(path_1)
interpreter.allocate_tensors()
# obtaining the input-output shapes and types
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


# INPUT SELECTION
# file selection window for input selection
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
input_img = Image.open(file_path)
# resizing input_img
input_img = input_img.resize((img_row, img_column))
# seperating the input image into constituent channels
red, green, blue = input_img.split()

# using channel blue in this case
x_matrix = np.array([np.array(blue)], 'f')
x_matrix = x_matrix.reshape(input_details[0]['shape'])
print(input_details[0]['shape'])


# RUNNING INTERPRETER
# setting the input tensor with the selected input
interpreter.set_tensor(input_details[0]['index'], x_matrix)

# running inference
interpreter.invoke()

y_matrix = interpreter.get_tensor(output_details[0]['index'])
print(y_matrix)
