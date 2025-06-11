import cv2
import numpy as np
import tensorflow as tf
import csv

# LOAD THE AI MODEL
#Our teaching machine model file will be named asl_model.h5
model = tf.keras.models.load_model('asl_model.h5')

def display_letters(file):
    """
    opens the file and converts letters to be displayed into list
    """
    letters = []
    with open(file, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            labels.append(row.strip())

display_letters('letters.txt')

# OPEN WEBCAM
#0 refer to computers default camera
cap = cv2.VideoCapture(0)

unprocessed = True
while unprocessed:
# cap.read(): This reads one frame from the camera. It returns two values:
# ret (short for "return"): A boolean value.
# True → frame was successfully read.
# False → frame read failed (e.g., camera not connected).
# frame: The actual image frame captured from the webcam (as a NumPy array).
    ret, frame = cap.read()
    if not ret:
        break

# Preprocess the image
img = cv2.resize(frame, (224, 224))
img_array = np.asarray(img, dtype=np.float32).reshape(1, 224, 224, 3)
img_array = (img_array / 127.5) - 1  # Normalize
    
