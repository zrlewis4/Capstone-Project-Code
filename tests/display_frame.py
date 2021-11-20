import numpy as np
import cv2

frame_no = 65
video = cv2.VideoCapture(r"C:\Users\Zachary Lewis\Documents\Bradley\Current\Capstone Project\Capstone Project Code\data\data_1.mp4")

video.set(1, frame_no)

ret, frame = video.read()
scale_percent = 60 # percent of original size
width = int(frame.shape[1] * scale_percent / 100)
height = int(frame.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

cv2.imshow('first frame', resized)

cv2.waitKey()

video.release()
cv2.destroyAllWindows()