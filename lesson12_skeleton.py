import cv2
import numpy as np

img = cv2.imread("mainimage.png", 0)

if img is None:
    print("Image not found")
    exit()

_, img = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)

size = np.size(img)
skeleton = np.zeros(img.shape, np.uint8)

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))

while True:

    eroded = cv2.erode(img, kernel)
    temp = cv2.dilate(eroded, kernel)

    temp = cv2.subtract(img, temp)
    skeleton = cv2.bitwise_or(skeleton, temp)

    img = eroded.copy()

    if cv2.countNonZero(img) == 0:
        break

cv2.imshow("Skeleton", img)
cv2.imshow("Skeleton", kernel)
cv2.imshow("Skeleton", skeleton)
cv2.waitKey(0)
cv2.destroyAllWindows()
