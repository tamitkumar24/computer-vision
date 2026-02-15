import cv2

img = cv2.imread("coin3.png")

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

for cnt in contours:

    hull = cv2.convexHull(cnt)

    # Draw contour
    cv2.drawContours(img, [cnt], -1, (0,255,0), 2)

    # Draw hull
    cv2.drawContours(img, [hull], -1, (0,0,255), 2)

cv2.imshow("Convex Hull", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
