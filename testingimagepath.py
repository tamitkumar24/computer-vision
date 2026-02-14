import cv2

img = cv2.imread("amit1.jpeg")   # change name to your image

# Check if loaded
if img is None:
    print("❌ Image not found! Check path.")
    exit()

img = cv2.resize(img, (500, 500))

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
