# Face-Detection-OpenCV

#### Face detection using Haar cascades is a machine learning based approach where a cascade function is trained with a set of input data. OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.

#### Some examples of pre-trained classifiers are:-

***haarcascade_frontalface_default.xml***

***haarcascade_frontal_cat_face.xml***

# Installation

First of all make sure you have Python installed in your system.

Secondly you have to install pip. It can be installed easily using command prompt.

    python -m pip install

The last requirement is the OpenCV module. It can be installed using pip.

    pip install opencv-python

# Detecting faces in Video/Image

Importing necessary Python & OpenCV libraries.

     import cv2

     import sys

### Declaring image path

     imagePath = 'Test_Image.jpg'

### ***INPUT IMAGES-***

![Test_Image](https://user-images.githubusercontent.com/86667690/127753679-e8f9fd0c-8322-4088-8f0f-8fb803769d88.jpg)

![Input_cats_Image](https://user-images.githubusercontent.com/86667690/127753692-fef110ee-3aca-4801-be1e-62402e396968.jpg)


### Reading image from image path

     image = cv2.imread(imagePath)

### Converting image to gray scale

The detection effectively works only on grayscale images. So it is important to convert the colour image to grayscale.

     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


### Using prebuilt XML classifiers

These are the pre-trained Classifiers that can be directly used. 

There are various Cascade classifiers available that can be used according to the requirement.

     faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

### Detecting faces

**detectMultiScale** function is used to detect the faces. It takes 3 arguments — the **input image, scaleFactor and minNeighbours**. **scaleFactor** specifies how much the image size is reduced with each scale. **minNeighbours** specifies how many neighbors each candidate rectangle should have to retain it.

    faces = faceCascade.detectMultiScale(

            gray,
    
            scaleFactor=1.3,
    
            minNeighbors=3,
    
            minSize=(30, 30)
    
            )

**faces** contains a list of coordinates for the rectangular regions where faces were found. We use these coordinates to draw the rectangles in our image.

    for(x, y, w, h) in faces:

      cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
     
### Saving output image

This is the final step of the code, there are two ways to get the output either we save the output image or directly view the output image.

    status = cv2.imwrite('faces_detected.jpg', image)

    print("[INFO] Image faces_detected.jpg written to filesystem: ", status)

### ***OUTPUT RESULTS-***

![Output_Image](https://user-images.githubusercontent.com/86667690/127753916-66bc4a19-90d4-4a76-945e-acbf104b24dc.jpg)

![Output_cats_image](https://user-images.githubusercontent.com/86667690/127753920-ba5199c3-81c5-4327-813f-2f4ca5069a04.jpg)

     
# Extracting faces from Video/Real Time

Importing necessary Python & OpenCV libraries.
          
          import cv2
          
          import random
          
          import os

**videoCapture** is used to capture video.

For capturing video in the real time using webcam-

          cap = cv2.VideoCapture(0)

For capturing or importing video from the saved files-

          cap = cv2.VideoCapture('video path')

Applying Loop Condition because of the continuity of the video.

          while True:

                _, img = cap.read()

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(gray, 1.1, 4)

                filename = str(random.randint(0,999))
    
         for (x, y, w, h) in faces:

                cv2.rectangle(img, (x, y), (x + w, y + h), (124, 255, 0), 2)
        
                roi_color = gray[y:y+h, x:x+w]

Declaring the path where the extracted faces will be saved.

                path = r'C:\Users\Lenovo\Desktop\Training'

Name by which extracted faces will be saved as jpg file.

                full_name = 'demo_{}.jpg'.format(count)
               
               os.chdir(path)
               
               cv2.imwrite(full_name, roi_color)
        
               print('Face Detected & Saved with filename {}'.format(count))
        
               count+=1

Displaying the video in real time scenario.

     cv2.imshow('Video', img)

Stopping the program if the escape key is pressed.

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

Release the VideoCapture object

    cap.release()    

# Author

### ***JITENDRA SINGH BISHT***
