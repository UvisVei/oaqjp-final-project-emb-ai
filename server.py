''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the output parameters from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant emotion']

    # Return a formatted string with the sentiment label and score
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is 'anger':\
    {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and \
    'sadness': {sadness}. The dominant emotion is joy."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":

    app.run(host="0.0.0.0", port = 5000, debug=True)
    