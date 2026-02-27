from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):

    body = await request.json()

    user_text = body["queryResult"]["queryText"]

    return {
        "fulfillmentText": f"You said: {user_text}"
    }