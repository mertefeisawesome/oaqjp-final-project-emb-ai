"""Emotion Detection library uses IBM's Watson AI library to detect emotions from text input"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_homepage():
    """Renders homepage for application"""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detection():
    """Uses EmotionDetection library to return detected emotions from text"""
    text_to_analyze = str(request.args.get("textToAnalyze"))
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return response["dominant_emotion"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
