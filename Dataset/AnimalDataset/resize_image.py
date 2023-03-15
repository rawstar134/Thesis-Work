import cv2
import os
directory_name = 'sixth'
for name in os.listdir(directory_name):
    image = cv2.imread(directory_name+'/'+name)
    modified_image = cv2.resize(image,(2048,1024),cv2.INTER_CUBIC)
    cv2.imwrite('sixth/'+name,modified_image)
    print(name)
