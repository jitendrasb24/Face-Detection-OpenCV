# Importing Libraries
import cv2
import sys

# Declaring path of image file
imagePath = 'Input_cats_Image.jpg'

# Reading image from image path
image = cv2.imread(imagePath)

# Using prebuilt XML Classifiers
faceCascade = cv2.CascadeClassifier('haarcascade_frontal_cat_face.xml')

# Converting image to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
)

# Draw rectangles on each detected face
for(x, y, w, h) in faces:
     cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)

# saving the output image
status = cv2.imwrite('Output_cats_image.jpg', image)
print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
