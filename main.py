from fastapi import FastAPI, HTTPException
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
    start_time = datetime.datetime.fromisoformat(start_time_str.replace('Z', '+00:00'))
    target_time = start_time - datetime.timedelta(minutes=5)
    
    # Start a coroutine to wait until the target time
    asyncio.create_task(wait_and_print(target_time))

    return {"message": "Webhook received and processing started"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
