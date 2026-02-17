import cv2
import numpy as np

# 1. Read image
img = cv2.imread("coin1.jpg")

if img is None:
    print("Image not found")
    exit()

# 2. Resize (optional)
img = cv2.resize(img, (600, 600))

# 3. Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 4. Blur (remove noise)
blur = cv2.GaussianBlur(gray, (5,5), 0)

# 5. Convert to binary
_, thresh = cv2.threshold(
    blur, 0, 255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# 6. Invert (if needed)
thresh = cv2.bitwise_not(thresh)

# 7. Morphology (clean image)
kernel = np.ones((7,7), np.uint8)

clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
clean = cv2.morphologyEx(clean, cv2.MORPH_CLOSE, kernel)

# 8. Find contours (objects)
contours, _ = cv2.findContours(
    clean,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# 9. Draw and count
count = 0

for cnt in contours:
    area = cv2.contourArea(cnt)

    if area > 2000:   # remove small noise
        count += 1
        cv2.drawContours(img, [cnt], -1, (0,255,0), 2)

# 10. Show count
cv2.putText(
    img,
    f"Count: {count}",
    (20,40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0,0,255),
    2
)

# 11. Show results
cv2.imshow("Original", img)
cv2.imshow("Binary", thresh)
cv2.imshow("Clean", clean)

cv2.waitKey(0)
cv2.destroyAllWindows()
