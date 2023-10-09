from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

IFTTT_WEBHOOK = os.environ.get('IFTTT_WEBHOOK')

@app.post("/trigger-bitroid-hello-GitGuardian/")
async def trigger_ifttt_webhook():
    base_url = f'https://maker.ifttt.com/trigger/bitroid_hello/with/key/{IFTTT_WEBHOOK}'

    payload = {
        'value1': 'GitGuardian found',
        'value2': 'some credentials checkin in your github repository',
        'value3': 'take necessary action'
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(base_url, json=payload)
        if response.status_code == 200:
            return {"message": "JSON payload sent successfully to IFTTT Webhook"}
        else:
            return {"message": f"Failed to send JSON payload. Status code: {response.status_code}"}
    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
