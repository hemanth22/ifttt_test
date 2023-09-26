import requests
import json
import os

IFTTT_WEBHOOK = os.environ.get('IFTTT_WEBHOOK')

base_url = f'https://maker.ifttt.com/trigger/bitroid_war_room/with/key/{IFTTT_WEBHOOK}'

headers1 = {
  'Content-Type': 'application/json'
}


payload = {
    "this": [
        {
            "is": {
                "some": ["test", "data"]
            }
        }
    ]
}



try:
    response = requests.post(base_url, headers=headers1, json=payload)
    if response.status_code == 200:
        print('JSON payload sent successfully to IFTTT Webhook')
    else:
        print(f'Failed to send JSON payload. Status code: {response.status_code}')
except Exception as e:
    print(f'An error occurred: {str(e)}')