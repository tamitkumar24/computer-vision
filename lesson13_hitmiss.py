import cv2
import numpy as np

img = cv2.imread("coin3.png", 0)

if img is None:
    print("Image not found")
    exit()

# Convert to binary
_, img = cv2.threshold(img, 25, 255, cv2.THRESH_BINARY)

# Convert to 0/1
img = img // 255

# Kernel
kernel = np.array([
    [0, 1, 0],
    [1,-1, 1],
    [0, 1, 0]
], dtype=np.int8)

# Hit-or-miss
hitmiss = cv2.morphologyEx(img, cv2.MORPH_HITMISS, kernel)

# Convert back
hitmiss = hitmiss * 255

cv2.imshow("Hit Miss", hitmiss)
cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2
# import numpy as np

# # -----------------------------
# # STEP 1: Read Image (Grayscale)
# # -----------------------------
# img = cv2.imread("coin3.png", 0)

# if img is None:
#     print("Image not found")
#     exit()

# cv2.imshow("1. Original", img)

# # -----------------------------
# # STEP 2: Apply Otsu Threshold
# # -----------------------------
# _, thresh = cv2.threshold(img, 0, 255,
#                           cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# cv2.imshow("2. Binary (Otsu)", thresh)


# # -----------------------------
# # STEP 3: Remove Noise (Opening)
# # -----------------------------
# kernel = np.ones((9,9), np.uint8)
# clean = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
# clean = cv2.medianBlur(clean, 5)


# cv2.imshow("3. Noise Removed", clean)

# # -----------------------------
# # STEP 4: Connected Components
# # -----------------------------
# num_labels, labels = cv2.connectedComponents(clean)

# print("Total Objects:", num_labels - 1)  # subtract background

# # Create colored output image
# label_hue = np.uint8(179 * labels / np.max(labels))
# blank_ch = 255 * np.ones_like(label_hue)
# colored = cv2.merge([label_hue, blank_ch, blank_ch])

# colored = cv2.cvtColor(colored, cv2.COLOR_HSV2BGR)
# colored[label_hue == 0] = 0  # background black

# cv2.imshow("4. Connected Components (Colored)", colored)

# # -----------------------------
# # STEP 5: Skeletonization
# # -----------------------------
# skeleton = np.zeros(clean.shape, np.uint8)
# temp_img = clean.copy()

# while True:
#     eroded = cv2.erode(temp_img, kernel)
#     temp = cv2.dilate(eroded, kernel)
#     temp = cv2.subtract(temp_img, temp)
#     skeleton = cv2.bitwise_or(skeleton, temp)
#     temp_img = eroded.copy()

#     if cv2.countNonZero(temp_img) == 0:
#         break

# cv2.imshow("5. Skeleton", skeleton)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
