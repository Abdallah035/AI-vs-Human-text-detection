from fastapi import FastAPI
from pydantic import BaseModel
from detect_AI import predict_text

app = FastAPI()

# Request body model
class TextRequest(BaseModel):
    text: str

# Health check / welcome endpoint
@app.get("/")
async def get_root():
    return {"message": "Hello from our API!"}

# Text prediction endpoint
@app.post("/predict/")
async def predict(request: TextRequest):
    predicted = predict_text(request.text)
    return predicted
