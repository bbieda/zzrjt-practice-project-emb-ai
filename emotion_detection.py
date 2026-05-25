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
    
    # Return the text attribute of the response object
    return response.text