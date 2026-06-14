import boto3
import json

def lambda_handler(event, context):
    try:
        # 1. Extract the text and target language from the Lex event
        # Using a helper variable to keep lines clean and avoid syntax errors
        intent = event['sessionState']['intent']
        input_text = intent['slots']['Text']['value']['interpretedValue'].strip()
        language_slot = intent['slots']['Language']['value']['interpretedValue']

        if not input_text:
            raise ValueError("Input text is empty.")

        # 2. Map the language names from Lex to ISO codes
        language_codes = {
            'Spanish': 'es',
            'German': 'de',
            'Italian': 'it'
        }

        target_code = language_codes.get(language_slot)
        if not target_code:
            raise ValueError(f"Language {language_slot} is not supported.")

        # 3. Call Amazon Translate
        translate = boto3.client('translate')
        response = translate.translate_text(
            Text=input_text,
            SourceLanguageCode="auto",
            TargetLanguageCode=target_code
        )

        translated_text = response.get('TranslatedText')

        # 4. Construct the Lex V2 response
        return {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    "name": intent['name'],
                    "slots": intent['slots'],
                    "state": "Fulfilled"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": f"The translation is: {translated_text}"
                }
            ]
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    "name": event['sessionState']['intent']['name'],
                    "state": "Failed"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": f"Something went wrong: {str(e)}"
                }
            ]
        }
