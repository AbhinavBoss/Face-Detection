# face detection on image
import cv2

#use Haarcascade xml file for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#read the image
img = cv2.imread('3.png')

#convert it into gray image for the working of the algorithm
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#use detectMultiScale() method to implement face detetction
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#loopinf through the face coordinates to draw the rectangle
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('img', img)
 
#wait to press a key and then exit. 
cv2.waitKey()
cv2.destroyAllWindows()
