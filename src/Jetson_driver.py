import os
import time
import re
import cv2
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib as plt
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential


def image_avg(video):
    value = []
    current = 0
    previous = 0

    while (True):

        ret, frame = video.read()

        if ret:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
            # move below to outside of loop based on stream dimensions
            scale_percent = 60 # percent of original size
            width = int(frame.shape[1] * scale_percent / 100)
            height = int(frame.shape[0] * scale_percent / 100)
            dim = (width, height)
            #resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

            value.append(np.mean(image[0:20,:]))
            if value[current] < value[previous] and value[current] < 80:
                for i in range(0,6):
                    ret, frame = video.read()
                resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
                save_image = resized
                previous = current
                break
        else:
            break
        current += 1
    return cv2.cvtColor(save_image, cv2.COLOR_BGR2RGB)

def color_predict(frame, model, class_names):
    im = Image.fromarray(frame, 'RGB')
    im = im.resize((180, 180))
    img_array = np.array(im)

    img_array = tf.expand_dims(img_array, 0) # Create a 4D tensor
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
    )

    return class_names[np.argmax(score)]

def send_label(label):

    return False

def main():
    #open serial connection

    model_loc = r"C:\Users\Zachary Lewis\Documents\Bradley\Current\Capstone Project\Capstone Project Code\src\Project Model"
    model = tf.keras.models.load_model(model_loc)
    class_names = ['Blue', 'Brown', 'Green', 'Orange', 'Red', 'Yellow']


    video = cv2.VideoCapture()

    try:
        while True:
            frame = image_avg(video)
            color_label = color_predict(frame, model, class_names)
            if(send_label(color_label)):
                print("Successfully sent!")
            else:
                print("Failed to send label.")
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()