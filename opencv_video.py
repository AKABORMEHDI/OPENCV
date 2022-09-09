import cv2
import numpy as np

cap = cv2.VideoCapture('venv/video.mp4')

while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == ord('q'): #this waitkey control the vitesse of reading the 'x' is slow more than 'q'
        break

cap.release()
cv2.destroyAllWindows()
# to represent the video in four window we will resizing the pixels

import cv2
import numpy as np

cap = cv2.VideoCapture('venv/video.mp4')

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame =  cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = smaller_frame #in the top_left
    image[height//2:, :width//2] = smaller_frame #in the bottem_left
    image[:height//2, width//2:] = smaller_frame #in the top_right
    image[height//2:, width//2:] = smaller_frame #in the bottom_right

    cv2.imshow('frame', image)

    if cv2.waitKey(5) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#finaly to rotate the windows

import cv2
import numpy as np

cap = cv2.VideoCapture('venv/video.mp4')

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame =  cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) #we can't rotate them with 90° cse the dimonsions is (320,240,3)
    image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)# so when we rotate themwith 90° the dimonsions will be (240,320,3)
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image)

    if cv2.waitKey(5) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# to drow somthing in the video

import cv2
import numpy as np

cap = cv2.VideoCapture('venv/video.mp4')

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0,0), (width,height), (225,0,0), 10) # (225,0,0) blue
    img = cv2.line(img, (0,height), (width,0), (0,225,0), 5) # (0,225,0) green
    img = cv2.rectangle(img,(160,120),(400,600),(0,0,225),2)# (0,0,225) red
    img = cv2.circle(img, (width//2,height//2),100,(128,128,128), -1) #(128,128,128) gray the -1 in tickness means coloroie all the circle
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(img, 'AKABOR MEHDI team', (0,height-100),font, 1,(0,0,128),4, cv2.LINE_8)# fontscale is like a tickness of the font

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# to convert the color _______________________________
import cv2
import numpy as np

cap = cv2.VideoCapture('venv/video.mp4')

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame', hsv)

    if cv2.waitKey(5) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#-------------------------------------------------------------