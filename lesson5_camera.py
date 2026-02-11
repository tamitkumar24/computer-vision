import cv2

# Open camera (0 = default webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not working!")
    exit()

while True:
    # Read frame
    ret, frame = cap.read()

    if not ret:
        break

    # Show video
    cv2.imshow("My Camera", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera
cap.release()
cv2.destroyAllWindows()
