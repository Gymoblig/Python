import cv2
import imutils
# Initialize the Hand tracking module using cv2.data.haarcascades
hand_cascade = cv2.CascadeClassifier("C:\haarcascade_hand.xml")

# Initialize video capture
cap = cv2.VideoCapture(2)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect hands in the frame
    hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected hands
    for (x, y, w, h) in hands:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # You can also add logic here to identify specific hand gestures or fingers

    # Display the frame with hand tracking
    cv2.imshow("Hand Tracking", imutils.resize(frame, width=800))


    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
