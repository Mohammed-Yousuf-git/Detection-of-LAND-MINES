# 	“The Gesture Cursor: Precision at Your Fingertips”
“Hey everyone! Welcome to our team’s exciting mini-project where we blend computer vision and data handling to create something truly interactive. We’re training a live model that transforms your fingertips into a dynamic cursor, allowing you to control your screen with just a wave of your hand!”
<img src="https://miro.medium.com/v2/resize:fit:1400/0*OfoZ60WfklcJji7O.jpg" alt="" />
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
    <h1>Gesture-Controlled Mouse Using OpenCV and Mediapipe</h1>
    <p>This project implements a hand-gesture-controlled mouse using a webcam, Mediapipe's hand-tracking library, and PyAutoGUI. It allows users to control mouse movements, perform clicks, and drag operations through hand gestures.</p>
    
   <h2>Features</h2>
    <ul>
        <li><strong>Hand Tracking:</strong> Utilizes Mediapipe's hand solutions for detecting and tracking hand landmarks in real-time.</li>
        <li><strong>Mouse Movement:</strong> The mouse cursor is controlled based on the position of the index finger tip.</li>
        <li><strong>Left Click and Drag:</strong> A pinch gesture (thumb and index finger tip close together) initiates a left click or starts dragging.</li>
        <li><strong>Right Click:</strong> A gesture using the index and middle fingers close together triggers a right click.</li>
        <li><strong>Real-Time Performance:</strong> Processes video frames from the webcam and performs actions instantaneously.</li>
    </ul>

  <h2>Prerequisites</h2>
    <ul>
        <li>Python 3.x</li>
        <li>OpenCV</li>
        <li>Mediapipe</li>
        <li>PyAutoGUI</li>
    </ul>

  <h2>Installation</h2>
    <p>Clone the repository and install dependencies:</p>
    <pre>
        git clone <repository-link>
        cd <repository-folder>
        pip install opencv-python mediapipe pyautogui
    </pre>

   <h2>Usage</h2>
    <ol>
        <li>Run the script: <code>python gesture_mouse.py</code></li>
        <li>Use the following gestures:
            <ul>
                <li><strong>Move Cursor:</strong> Move your index finger in front of the camera.</li>
                <li><strong>Left Click/Drag:</strong> Pinch gesture (thumb and index finger tip close).</li>
                <li><strong>Right Click:</strong> Bring index and middle finger tips close together.</li>
            </ul>
        </li>
        <li>Press <code>q</code> to quit the program.</li>
    </ol>

   <h2>Acknowledgments</h2>
    <ul>
        <li><a href="https://mediapipe.dev/">Mediapipe</a> for its robust hand-tracking library.</li>
        <li><a href="https://pyautogui.readthedocs.io/">PyAutoGUI</a> for mouse automation.</li>
    </ul>

  <h2>Note</h2>
    <p>Adjust thresholds and calibration in the script to suit different lighting and camera setups.</p>
</body>
</html>
