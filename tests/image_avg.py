import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

video = cv2.VideoCapture(r"C:\Users\Zachary Lewis\Documents\Bradley\Current\Capstone Project\Capstone Project Code\data\test_intensity.mp4")
value = []

while (True):

    ret, frame = video.read()

    if ret:
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Live", image)
        value.append(np.mean(frame.astype(float)))
    else:
        break
    #key = cv2.waitKey(1)
    #if key == ord("q"):
    #    break
    

video.release()


plt.plot(value)
plt.xlabel('Number of Frames')
plt.ylabel('Frame average')
plt.show()