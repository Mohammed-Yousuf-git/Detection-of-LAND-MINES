import cv2
import mediapipe as mp
import pyautogui
import math

# Mediapipe hands setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Screen size for pyautogui (used to scale hand positions to screen size)
screen_width, screen_height = pyautogui.size()

# Mouse action flags
is_dragging = False
running = False  # Control flag for stopping the loop

# Function to calculate the distance between two landmarks
def calculate_distance(landmark1, landmark2):
    return math.sqrt((landmark1.x - landmark2.x) ** 2 + (landmark1.y - landmark2.y) ** 2)

# Function to move mouse based on hand position
def move_mouse(index_finger_x, index_finger_y):
    screen_x = int(index_finger_x * screen_width)
    screen_y = int(index_finger_y * screen_height)
    pyautogui.moveTo(screen_x, screen_y)
    print(f"Mouse moved to: ({screen_x}, {screen_y})")

# Function to perform left click
def left_click_mouse():
    pyautogui.click()
    print("Left click")

# Function to perform right click
def right_click_mouse():
    pyautogui.click(button='right')
    print("Right click")

# Hand gesture detection function
def detect_hand_gestures():
    global is_dragging, running

    cap = cv2.VideoCapture(0)  # Initialize webcam

    with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
        while cap.isOpened() and running:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            # Flip the frame horizontally for natural movement
            frame = cv2.flip(frame, 1)

            # Convert the BGR image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Process the image and detect hands
            results = hands.process(image)

            # Convert the RGB image back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # Get the index finger tip and thumb tip landmarks
                    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

                    # Get normalized hand coordinates for index finger tip
                    index_finger_x = index_finger_tip.x
                    index_finger_y = index_finger_tip.y

                    # Calculate the distance between thumb and index finger tip for pinch gesture
                    pinch_distance = calculate_distance(index_finger_tip, thumb_tip)

                    # Perform left-click if a pinch is detected (thumb close to index finger)
                    if pinch_distance < 0.05:
                        if not is_dragging:
                            left_click_mouse()
                            pyautogui.mouseDown()
                            is_dragging = True
                    else:
                        if is_dragging:
                            pyautogui.mouseUp()
                            is_dragging = False

                    # Right-click gesture: use a specific distance threshold to detect right-click
                    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                    right_click_distance = calculate_distance(index_finger_tip, middle_finger_tip)

                    if right_click_distance < 0.05:
                        right_click_mouse()

                    # Move mouse based on index finger tip position
                    move_mouse(index_finger_x, index_finger_y)

            # Display the frame in a separate window
            cv2.imshow("Hand Gesture Detection", image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
