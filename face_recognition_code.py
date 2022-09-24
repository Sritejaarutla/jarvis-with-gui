def face_recogniton():
    import cv2

    recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
    recognizer.read('trainer/trainer.yml')  # load trained model
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)  # initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type

    id = 2  # number of persons you want to Recognize
    #if 1.1 to 1.300 taken =kiran samples then it is kiran ,if 2.1 to 2.300=teja reddy photo samples then it is teja reddy like this list continues
    names = ['', 'kiran',"sri teja","waste fellow ","abu",'pramod']  # names, leave first empty bcz counter starts from 0

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW to remove warning
    cam.set(3, 640)  # set video FrameWidht
    cam.set(4, 480)  # set video FrameHeight

    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    # flag = True

    while True:

        ret, img = cam.read()  # read the frames using the above created object

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # used to draw a rectangle on any image

            id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])  # to predict on every single image

            # Check if accuracy is less than 100 ==> 40 is perfect match
            ''' we are taking greater than 40 becuz sometimes for other persons accuracy will be 10 to 40 accuracy
                depends upon on the camera quality in which sample photos are taken
                if their is only one person sample then the model cannot distinguish between
                different peoples so train more images add more images in samples either from internet or 
                from camera but sequence must be 1.1, 2.1,3.1 etc each person should have unique sequence'''

            if (accuracy < 100 and accuracy>=35):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)
        # used for camera moment if u keep it k=100 or 1000 the camera moment will be very slow for eg if u move ur face it will reflect after 100milliseconds
        k = cv2.waitKey(10)

        # press q to exit if we dont write this statement the camera will not stop until we stop the code(no keys will work)
        if k == ord("q") or k==ord("Q"):# Press 'q' for exiting video for esc use k==27
            break

    print("face recognition code execution complted.")
    cam.release()
    cv2.destroyAllWindows()
# face_recogniton()












