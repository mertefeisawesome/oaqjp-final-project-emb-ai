from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, render_template, request

app = Flask("Emotion Detector")


@app.route("/")
def render_homepage():
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detection():
    text_to_analyze = str(request.args.get("textToAnalyze"))
    response = emotion_detector(text_to_analyze)
    print(response)

    return response["dominant_emotion"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
