import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set up the headers required by the Watson API
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Create the payload with the input text
    input_json = { 
        "raw_document": { 
            "text": text_to_analyze 
        } 
    }
    
    # Make the POST request to the service
    response = requests.post(url, json=input_json, headers=headers)
    
    # Check the status code for a blank entry / bad request
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Proceed normally if the status code is 200 (Success)
    formatted_response = json.loads(response.text)
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotion_predictions['anger']
    disgust_score = emotion_predictions['disgust']
    fear_score = emotion_predictions['fear']
    joy_score = emotion_predictions['joy']
    sadness_score = emotion_predictions['sadness']
    
    emotions_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    emotions_dict['dominant_emotion'] = dominant_emotion
    
    return emotions_dict