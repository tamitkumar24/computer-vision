import cv2
import numpy as np

img = cv2.imread("ashi.jpg", 0)

if img is None:
    print("Image not found")
    exit()

_, thresh = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

kernel = np.ones((5,5), np.uint8)

# Erosion
erode = cv2.erode(thresh, kernel, iterations=1)

cv2.imshow("Original", thresh)
cv2.imshow("Erosion", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
