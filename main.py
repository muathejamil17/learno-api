"""
POC to integrate with learnosity.
"""
from fastapi import FastAPI, Query
from services.learnosity_service import LearnosityService
from models.learnosity_models import Question
from configs.settings import Settings
app = FastAPI()


settings = Settings()

learnosity_svc = LearnosityService(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.DOMAIN,
                                   settings.QUESTIONS_ENDPOINT)





@app.get("/")
async def root():
    """
    Root Endpoint.
    Args: 
    Returns: dictionary 
    """
    return {"message": "Hello World"}


@app.get("/questions")
async def get_item(item_reference: str, organization_id: int = Query(..., description="ID of the item bank")):
    return await learnosity_svc.get_item(item_reference, organization_id)


@app.post("/questions")
async def create_item(question_create_request: Question):
    return await learnosity_svc.create_item(question_create_request, settings.ORGANIZATION_ID)
