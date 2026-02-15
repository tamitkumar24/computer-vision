import cv2
import numpy as np

img = cv2.imread("coin3.png", 0)

if img is None:
    print("Image not found")
    exit()

# 1️⃣ Blur first
blur = cv2.GaussianBlur(img, (5,5), 0)

# 2️⃣ Otsu threshold
_, thresh = cv2.threshold(
    blur, 0, 255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

kernel = np.ones((3,3), np.uint8)

# 3️⃣ Remove small noise
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# 4️⃣ Fill small holes
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

# 5️⃣ Optional prune
eroded = cv2.erode(closing, kernel, iterations=2)
pruned = cv2.dilate(eroded, kernel, iterations=2)

cv2.imshow("Original", img)
cv2.imshow("Threshold", thresh)
cv2.imshow("Cleaned", closing)
cv2.imshow("Pruned", pruned)

cv2.waitKey(0)
cv2.destroyAllWindows()
