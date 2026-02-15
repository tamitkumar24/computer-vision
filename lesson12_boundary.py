import cv2
import numpy as np

img = cv2.imread("boys.jpeg", 0)

if img is None:
    print("Image not found")
    exit()

# Binary
_, thresh = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)

kernel = np.ones((3,3), np.uint8)

# Erosion
eroded = cv2.erode(thresh, kernel, 1)

# Boundary
boundary = thresh - eroded

cv2.imshow("original", img)
cv2.imshow("Binary", thresh)
cv2.imshow("Boundary", boundary)

cv2.waitKey(0)
cv2.destroyAllWindows()
