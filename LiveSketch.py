import cv2


def sketch(image):
    GrayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    RemoveNoise = cv2.GaussianBlur(GrayImage,(5,5),0)

    CannyEdge = cv2.Canny(RemoveNoise,15,100)

    ret,ThesholdImage = cv2.threshold(CannyEdge,100,255,cv2.THRESH_BINARY_INV)

    return ThesholdImage




Video = cv2.VideoCapture(0)

while True:
    ret, frame = Video.read()
    cv2.imshow("Live Sketch" , sketch(frame))
    if(cv2.waitKey(1)==13):
        break

Video.release()
cv2.destroyAllWindows()