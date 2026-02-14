import cv2

# Open camera
cap = cv2.VideoCapture(0)

# Read first frame
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():

    # Difference between frames
    diff = cv2.absdiff(frame1, frame2)

    # Convert to gray
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Blur
    blur = cv2.GaussianBlur(gray, (9,9), 0)

    # Threshold
    _, thresh = cv2.threshold(blur, 35, 255, cv2.THRESH_BINARY)

    # Dilate (make white area bigger)
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find contours
    contours, _ = cv2.findContours(
        dilated,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    count = 0

    for cnt in contours:

        # Ignore small movements
        if cv2.contourArea(cnt) < 2500:
            continue

        count += 1

        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame1, (x,y), (x+w,y+h), (0,255,0), 2)

    # Show count
    cv2.putText(
        frame1,
        f"Moving Objects: {count}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        2
    )

    cv2.imshow("Camera", frame1)

    # Update frames
    frame1 = frame2
    ret, frame2 = cap.read()

    # Quit with q
    if cv2.waitKey(30) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
