# importing libraries

import cv2
import random
import os

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)

count = 1

while True:

    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    filename = str(random.randint(0,999))
    # Draw the rectangle around each face

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (124, 255, 0), 2)
        roi_color = gray[y:y+h, x:x+w]

        # Path where faces will be saved
        path = r'C:\Users\Lenovo\Desktop\Training'

        # Name by which faces will be saved as jpg file
        full_name = 'demo_{}.jpg'.format(count)
        os.chdir(path)
        cv2.imwrite(full_name, roi_color)
        print('Face Detected & Saved with filename {}'.format(count))
        count+=1


        # Display
    cv2.imshow('Video', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    # Release the VideoCapture object
cap.release()