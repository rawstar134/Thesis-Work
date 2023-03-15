import os
import cv2

#read the frames from the video
path = 'sixth_video.mp4'
vidObj = cv2.VideoCapture(path)
count = 1
success  = 1
while success :
    success, image = vidObj.read()
    # print(image)
    if success == True:
        name = 'sixth/'+str(count)+'.jpg'
        cv2.imwrite(name,image)
        count = count + 1
    else:
        break
