import cv2
import numpy as np

img = cv2.imread("coin1.jpg", 0)

if img is None:
    print("Image not found")
    exit()

# Blur to remove details
blur = cv2.GaussianBlur(img, (7,7), 0)

# Better threshold
_, thresh = cv2.threshold(
    blur, 0, 255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# Strong noise removal
kernel = np.ones((5,5), np.uint8)

opening = cv2.morphologyEx(
    thresh,
    cv2.MORPH_OPEN,
    kernel,
    iterations=3
)

# Fill holes
closing = cv2.morphologyEx(
    opening,
    cv2.MORPH_CLOSE,
    kernel,
    iterations=3
)

# Background
sure_bg = cv2.dilate(closing, kernel, iterations=3)

# Foreground
dist = cv2.distanceTransform(closing, cv2.DIST_L2, 5)

_, sure_fg = cv2.threshold(
    dist,
    0.6 * dist.max(),
    255,
    0
)

sure_fg = np.uint8(sure_fg)

unknown = cv2.subtract(sure_bg, sure_fg)

# Markers
_, markers = cv2.connectedComponents(sure_fg)

markers = markers + 1
markers[unknown == 255] = 0

# Watershed
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

markers = cv2.watershed(color, markers)

# Draw boundary
color[markers == -1] = [0,0,255]

# Show
cv2.imshow("Original", img)
cv2.imshow("Binary", thresh)
cv2.imshow("Cleaned", closing)
cv2.imshow("Segmented", color)

cv2.waitKey(0)
cv2.destroyAllWindows()



























# import cv2
# import numpy as np

# # Load image in grayscale
# img = cv2.imread("coin1.jpg", 0)

# # Check image
# if img is None:
#     print("Image not found")
#     exit()

# # Convert to binary
# _, thresh = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY_INV)

# # Remove noise
# kernel = np.ones((3,3), np.uint8)
# opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# # Find sure background
# sure_bg = cv2.dilate(opening, kernel, iterations=3)

# # Find sure foreground
# dist = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# _, sure_fg = cv2.threshold(dist, 0.5*dist.max(), 255, 0)

# # Convert to uint8
# sure_fg = np.uint8(sure_fg)

# # Find unknown region
# unknown = cv2.subtract(sure_bg, sure_fg)

# # Label markers
# _, markers = cv2.connectedComponents(sure_fg)

# markers = markers + 1
# markers[unknown == 255] = 0

# # Apply watershed
# color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# markers = cv2.watershed(color_img, markers)

# # Draw boundaries
# color_img[markers == -1] = [0,0,255]

# # Show result
# cv2.imshow("Original", img)
# cv2.imshow("Binary", thresh)
# cv2.imshow("Segmented", color_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
