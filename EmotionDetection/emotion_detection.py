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
    
    # Convert the response text into a dictionary using the json library
    formatted_response = json.loads(response.text)
    
    # Extract the emotion predictions block from the Watson response structure
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extract the required set of emotions and their scores
    anger_score = emotion_predictions['anger']
    disgust_score = emotion_predictions['disgust']
    fear_score = emotion_predictions['fear']
    joy_score = emotion_predictions['joy']
    sadness_score = emotion_predictions['sadness']
    
    # Isolate the targeted emotions into a dictionary to easily find the dominant one
    emotions_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Logic to find the dominant emotion (the key with the maximum value)
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    
    # Append the dominant emotion to the final output structure
    emotions_dict['dominant_emotion'] = dominant_emotion
    
    # Return the formatted dictionary
    return emotions_dict