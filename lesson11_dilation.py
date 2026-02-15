import cv2
import numpy as np

img = cv2.imread("ashi.jpg", 0)   # Read in gray

if img is None:
    print("Image not found")
    exit()

# Convert to binary
_, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)

# Kernel
kernel = np.ones((5,5), np.uint8)

# Dilation
dilate = cv2.dilate(thresh, kernel, iterations=1)

cv2.imshow("Original", thresh)
cv2.imshow("Dilation", dilate)

cv2.waitKey(0)
cv2.destroyAllWindows()
