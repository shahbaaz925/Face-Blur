import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the video capture
cap = cv2.VideoCapture(0)  # 0 for default camera, you can change it to a video file path if needed

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop through detected faces
    for (x, y, w, h) in faces:
        # Get the position of the detected face
        face_position = (x, y, x + w, y + h)

        # Extract the region of interest (ROI) for the face
        face_roi = frame[y:y + h, x:x + w]

        # Apply Gaussian blur to the face ROI
        blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 30)

        # Replace the face ROI with the blurred version
        frame[y:y + h, x:x + w] = blurred_face

    # Display the frame with detected faces
    cv2.imshow('Face Detection and Blurring', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
