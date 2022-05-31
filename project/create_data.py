# Creating database
# It captures images and stores them in datasets
# folder under the folder name of sub_data
import cv2, sys, numpy, os
haar_file = 'haarcascade_frontalface_default.xml'

# All the faces data will be
# present this folder
datasets = 'datasets'


#we need a function to make it easier to add new people
def addPeople():
        # These are sub data sets of folder,
        # for my faces I've used my name you can
        # change the label here
        sub_data = input("enter the name of the person")	

        path = os.path.join(datasets, sub_data)
        print(path)
        if not os.path.isdir(path):
                os.mkdir(path)

        # defining the size of images
        (width, height) = (130, 100)

        #'0' is used for my webcam,
        # if you've any other camera
        # attached use '1' like this
        face_cascade = cv2.CascadeClassifier(haar_file)
        webcam = cv2.VideoCapture(0)

        # The program loops until it has 30 images of the face.
        count = 1
        while count < 30:
                (_, im) = webcam.read()
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 4)
                for (x, y, w, h) in faces:
                        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        face = gray[y:y + h, x:x + w]
                        face_resize = cv2.resize(face, (width, height))
                        cv2.imwrite('% s/% s.png' % (path, count), face_resize)
                count += 1
                
                cv2.imshow('OpenCV', im)
                key = cv2.waitKey(10)
                if key == 27:
                        break

        webcam.release()

        cv2.destroyAllWindows()



while True:
        option = input("""Do you want to add another person?
        Options:
        Enter 'yes' or 'no'

        """)
        if option == "yes":
                addPeople()
        else:
                break



