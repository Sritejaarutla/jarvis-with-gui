import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if ret == False:
        break
    # getting width and height of image
    height, width, _ = frame.shape

    # creating copy of image using resize function
    resziedImage = cv2.resize(frame, (width, height),
                             interpolation=cv2.INTER_AREA)

    # creating 3X3 kernel, inorder to sharpen the image /frame
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    # Appling kernel on the frame using filter2D function .
    sharpenImage = cv2.filter2D(resziedImage, -1, kernel)

    # converting image into Grayscale image.
    gray = cv2.cvtColor(sharpenImage, cv2.COLOR_BGR2GRAY)

    # creating inverse of sharpen image .
    inverseImage = 255-gray

    # applying Gussain Blur on the image .
    bluredImage = cv2.GaussianBlur(inverseImage, (15, 15), 0, 0)

    # create a pencilSketch using divide function on opencv .
    pencilSketch = cv2.divide(gray, 255-bluredImage, scale=256)

    # show the frame on the screen .
    #cv.imshow('Sharpen Image', sharpenImage)
    cv2.imshow("pencilSketch", pencilSketch)

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
camera.release()