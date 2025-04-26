import requests
import json


def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url=url, headers=headers, json=input_json)
    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    emotion_scores = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
    }
    dominant_emotion = ""
    max_score = 0

    for key, value in emotion_scores.items():
        if value > max_score:
            max_score = value
            dominant_emotion = key

    emotion_scores["dominant_emotion"] = dominant_emotion

    return emotion_scores


if __name__ == "__main__":
    print(emotion_detector("i love this new technology"))
