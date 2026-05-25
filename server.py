from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Renders the main application page using the index.html template.
    """
    return render_template('index.html')

# CHANGE THIS LINE FROM /emotionDetector TO /sentimentAnalyzer
@app.route("/sentimentAnalyzer")
def emotion_detector_route():
    """
    Processes the text submitted by the user, runs emotion detection,
    and returns a formatted string response to the frontend.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Run emotion detection using the packaged function
    response = emotion_detector(text_to_analyze)
    
    # Extract the individual scores and dominant emotion
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Format the output string exactly matching the customer's requirement
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    
    return formatted_response

if __name__ == "__main__":
    # Deploy the application on localhost:5000
    app.run(host="0.0.0.0", port=5000)