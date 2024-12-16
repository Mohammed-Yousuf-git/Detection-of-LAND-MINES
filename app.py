from flask import Flask, render_template, redirect, url_for
from threading import Thread
import hand_gesture_mouse

app = Flask(__name__)
detection_thread = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start")
def start_detection():
    global detection_thread
    if detection_thread is None or not detection_thread.is_alive():
        hand_gesture_mouse.running = True
        detection_thread = Thread(target=hand_gesture_mouse.detect_hand_gestures)
        detection_thread.start()
    return redirect(url_for("index"))

@app.route("/stop")
def stop_detection():
    hand_gesture_mouse.running = False
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
