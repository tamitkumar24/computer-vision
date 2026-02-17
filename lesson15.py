import cv2
import numpy as np

# Load image
img = cv2.imread("coin1.jpg")

if img is None:
    print("Image not found")
    exit()

# Convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur
blur = cv2.GaussianBlur(gray, (5,5), 0)

# Threshold (Otsu)
_, thresh = cv2.threshold(
    blur, 0, 255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# Remove noise
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(
    thresh, cv2.MORPH_OPEN, kernel, iterations=2
)

# Background
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Foreground
dist = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(
    dist, 0.7*dist.max(), 255, 0
)

sure_fg = np.uint8(sure_fg)

# Unknown area
unknown = cv2.subtract(sure_bg, sure_fg)

# Marker labeling
_, markers = cv2.connectedComponents(sure_fg)

markers = markers + 1
markers[unknown == 255] = 0

# Watershed
markers = cv2.watershed(img, markers)

# Draw borders
img[markers == -1] = [0,0,255]

# Count objects
count = len(np.unique(markers)) - 2

print("Objects:", count)

# Show
cv2.imshow("Original", img)
cv2.imshow("Threshold", thresh)
cv2.imshow("Opening", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
