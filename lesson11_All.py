import cv2
import numpy as np

img = cv2.imread("coin1.jpg", 0)

if img is None:
    print("Image not found")
    exit()

_, thresh = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

kernel = np.ones((5,5), np.uint8)

dilate = cv2.dilate(thresh, kernel, 1)
erode = cv2.erode(thresh, kernel, 1)

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Binary", thresh)
cv2.imshow("Dilation", dilate)
cv2.imshow("Erosion", erode)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
