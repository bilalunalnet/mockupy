import numpy as np
import cv2

img = cv2.imread('deneme.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(imgray, (5, 5), 0)
thresh = cv2.threshold(blurred, 192, 255, cv2.THRESH_BINARY)[1]
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(hierarchy[0])):
    print(i, ":", hierarchy[0][i])
new = cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imshow("deneme",new)
cv2.waitKey(0)
cv2.destroyAllWindows()