import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
from scipy.signal import find_peaks

video = cv2.VideoCapture(r"C:\Users\Zachary Lewis\Documents\Bradley\Current\Capstone Project\Capstone Project Code\data\data_1.mp4")
value = []
current = 0
previous = 0

#video.set(1, 310)

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
            for i in range(0,5):
                ret, frame = video.read()
            resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
            save_image = resized
            previous = current
            break
    else:
        break
    current += 1

video.release()

#cv2.imwrite(r"C:\Users\Zachary Lewis\Documents\Bradley\Current\Capstone Project\Capstone Project Code\data\saved_frame.jpg", save_image)
save_image = cv2.cvtColor(save_image, cv2.COLOR_BGR2RGB)
plt.figure("Good frame")
plt.imshow(save_image)
key = cv2.waitKey()



plt.figure("Frame average over time")
plt.plot(value)
plt.xlabel('Number of Frames')
plt.ylabel('Frame average')
plt.show()