import os
import time
import re
import cv2
import tensorflow as tf
import numpy as np
import PIL
import matplotlib as plt
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

model_loc = r"C:\Users\Zachary Lewis\Documents\Bradley\Current\Capstone Project\Capstone Project Code\src\Project Model"

model = tf.keras.models.load_model(model_loc)

def sorted_nicely( l ): 
    """ Sort the given iterable in the way that humans expect.""" 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

test_url = r"C:\Users\Zachary Lewis\Documents\Bradley\Current\Capstone Project\Capstone Project Code\data\network test data"

class_names = ['Blue', 'Brown', 'Green', 'Orange', 'Red', 'Yellow']

for filename in sorted_nicely(os.listdir(test_url)):
  file = os.path.join(test_url, filename)
  if os.path.isfile(file):
    img = keras.preprocessing.image.load_img(
    file, target_size=(180, 180)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
    )
    time.sleep(0.1)