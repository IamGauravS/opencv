import cv2
import numpy as np
#windowName = "Live feed"


cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()

else:
    ret = False

while ret:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #blucolor
    #low = np.array([100,50,50])
    #high = np.array([140,255,255])

    #greencolor
    #low = np.array([40,50,50])
    #high = np.array([80, 255, 255])

    #redcolor
    low = np.array([0,70,50])
    high = np.array([10,255, 255])

    image_mask = cv2.inRange(hsv, low, high)
    output = cv2.bitwise_and(frame, frame, mask= image_mask)
    cv2.imshow("mask", image_mask)

    cv2.imshow("original", frame)

    cv2.imshow("color tracking", output)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
VideoFileOutput.release()
cap.release()