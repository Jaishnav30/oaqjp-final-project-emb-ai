"""
Flask web application for emotion detection using the emotion_detector module.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Renders the index HTML page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emo_detector():
    """
    Handles emotion detection requests.
    Returns emotion scores and dominant emotion for the given text.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    emo = emotion_detector(text_to_analyze)

    if emo["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is:\n"
        f"  anger: {emo['anger']},\n"
        f"  disgust: {emo['disgust']},\n"
        f"  fear: {emo['fear']},\n"
        f"  joy: {emo['joy']},\n"
        f"  sadness: {emo['sadness']}.\n"
        f"The dominant emotion is {emo['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

