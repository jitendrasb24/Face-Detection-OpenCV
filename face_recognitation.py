# importing opencv libraries
import cv2
import sys

# declaring image path
imagePath = 'Test_Image.jpg'

# reading image from image path
image = cv2.imread(imagePath)

# converting image to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# using prebuilt XML classifiers
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# detecting faces
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
)

for(x, y, w, h) in faces:
     cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)

# saving output image
status = cv2.imwrite('faces_detected.jpg', image)
print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
