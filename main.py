import cv2
import tensoreflow as tf
import numpy as np
import csv

#Load the AI model
#Our teaching machine model file will be named keras_model.h5
model = tf.keras.models.load_model('keras_model.h5')

#Making labels
# We need a labels.txt file
labels = []
with open('labels.txt', mode='r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            labels.append(row.strip())
