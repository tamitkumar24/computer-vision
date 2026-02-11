import cv2

# Load image
img = cv2.imread("ashi.jpg")

if img is None:
    print("Image not found!")
    exit()

# Show original image
cv2.imshow("Original", img)

# Print image shape
print("Image Shape:", img.shape)

# Resize image (width, height)
resized = cv2.resize(img, (600, 500))
cv2.imshow("Resized", resized)

# Convert to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("Gray shape",gray.shape)
# cv2.imshow("Grayscale", gray)

# Read one pixel value (row, col)
pixel = img[200, 200]
print("Pixel at (100,100):", pixel)
 
# Apply Blur
blur = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("Blur", blur)

# Edge Detection
# edges = cv2.Canny(blur, 50, 150) 
# cv2.imshow("Edges", edges)

# Simple Threshold
# _, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)

#Normal threshold fails in bad light.
#So we use:
adaptive = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    21, 5
)

cv2.imshow("Gray", gray)
# cv2.imshow("Threshold", thresh)
cv2.imshow("Threshold", adaptive)
#put it below wait key
# Find contours
contours, _ = cv2.findContours(
    adaptive,
    # cv2.RETR_EXTERNAL
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
)

# Draw contours
result = img.copy()
cv2.drawContours(result, contours, -1, (0,0,255), 5)
contours1, _ = cv2.findContours(adaptive, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("External:", len(contours1))

contours2, hierarchy = cv2.findContours(adaptive, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("Tree:", len(contours2))

print("Objects found:", len(contours))
cv2.imshow("Contours", result)
# area = cv2.contourArea(result)
# print(area)

# Wait
cv2.waitKey(0)


cv2.destroyAllWindows()


