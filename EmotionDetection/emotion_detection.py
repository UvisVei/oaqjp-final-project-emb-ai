import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        emotion_dictionary = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,
        'joy': joy_score, 'sadness': sadness_score}

        dominant_value = 0
        for emotion, value in emotion_dictionary.items():
            if value > dominant_value:
                dominant_value = value
                dominant_emotion = emotion
        
        emotion_dictionary.update({'dominant emotion': dominant_emotion})

    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
        
        emotion_dictionary = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,
        'joy': joy_score, 'sadness': sadness_score, 'dominant emotion': dominant_emotion}

    return emotion_dictionary