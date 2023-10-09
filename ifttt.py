from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

IFTTT_WEBHOOK = os.environ.get('IFTTT_WEBHOOK')

class Reminder(BaseModel):
    value1: str
    value2: str
    value3: str

@app.post("/trigger-bitroid-hello/")
async def trigger_ifttt_webhook(reminder: Reminder):
    base_url = f'https://maker.ifttt.com/trigger/bitroid_hello/with/key/{IFTTT_WEBHOOK}'

    payload = {
        'value1': reminder.value1,
        'value2': reminder.value2,
        'value3': reminder.value3
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
