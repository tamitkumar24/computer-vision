# import cv2
# import numpy as np

# img = cv2.imread("coin1.jpg", 0)

# if img is None:
#     print("Image not found")
#     exit()

# # Blur to remove noise
# blur = cv2.GaussianBlur(img, (5,5), 0)

# # Adaptive threshold
# thresh = cv2.adaptiveThreshold(
#     blur, 255,
#     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#     cv2.THRESH_BINARY_INV,
#     11, 2
# )
# kernel = np.ones((3,3), np.uint8)

# binary = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
# binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# # Find connected components
# num, labels = cv2.connectedComponents(thresh)

# print("Total Objects:", num-1)

# # Show labels
# labels_img = (labels * 255 / labels.max()).astype("uint8")

# cv2.imshow("Binary", thresh)
# cv2.imshow("Components", labels_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

# Read grayscale
img = cv2.imread("coin1.jpg", 0)

if img is None:
    print("Image not found")
    exit()

# Blur (remove texture)
blur = cv2.GaussianBlur(img, (9,9), 0)

# OTSU Threshold
_, binary = cv2.threshold(
    blur, 0, 255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# Kernel
kernel = np.ones((7,7), np.uint8)

# Fill coins
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# Fill holes inside coins
binary = cv2.morphologyEx(binary, cv2.MORPH_DILATE, kernel)

# Connected components
num, labels = cv2.connectedComponents(binary)

print("Total Coins:", num-1)

# Display labels
labels_img = (labels * 255 / labels.max()).astype("uint8")

# Show
cv2.imshow("Binary", binary)
cv2.imshow("Components", labels_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

