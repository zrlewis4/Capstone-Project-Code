import cv2

vidcap = cv2.VideoCapture(r"C:\Users\Zachary Lewis\Documents\Bradley\Current\Capstone Project\Capstone Project Code\data\network train data\broken7.mp4")
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite(r"C:\Users\Zachary Lewis\Documents\Bradley\Current\Capstone Project\Capstone Project Code\data\network train data\Broken\frame7%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1