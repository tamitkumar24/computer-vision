import cv2

# Read image
img = cv2.imread("coin1.jpg")   # Put your image name here

# Resize (optional)
img = cv2.resize(img, (500, 400))

# Convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur to remove noise
blur = cv2.GaussianBlur(gray, (7, 7), 0)

# Convert to black & white
_, thresh = cv2.threshold(blur, 210, 255, cv2.THRESH_BINARY_INV)

# Find contours (objects)
contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Count objects
count = len(contours)

# Draw contours
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Show count
cv2.putText(
    img,
    f"Objects: {count}",
    (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 255),
    2
)

# Show windows
cv2.imshow("Original", img)
cv2.imshow("Threshold", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
