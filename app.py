from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import datetime
import asyncio

app = FastAPI()

class WebhookData(BaseModel):
    startTime: str

async def wait_and_print(target_time):
    """ Waits until the target time and prints it. """
    now = datetime.datetime.utcnow()
    wait_seconds = (target_time - now).total_seconds()
    if wait_seconds > 0:
        await asyncio.sleep(wait_seconds)
    print(f"Time reached: {target_time.isoformat()}Z")

@app.post("/webhook")
async def webhook(data: WebhookData):
    """ Receives a webhook and processes the time. """
    start_time_str = data.startTime
    
    if not start_time_str:
        raise HTTPException(status_code=400, detail="startTime not provided")
    
    # Parse the start time and subtract 5 minutes
    start_time = datetime.dateti
