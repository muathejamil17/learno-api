"""
POC to integrate with learnosity.
"""
from fastapi import FastAPI, Query
from services.learnosity_service import LearnosityService
from models.learnosity_models import Question, LearnosityTag
from configs.settings import Settings
from typing import List

app = FastAPI()



settings = Settings()

learnosity_svc = LearnosityService(
    settings.CONSUMER_KEY,
    settings.CONSUMER_SECRET,
    settings.DOMAIN,
    settings.DATA_BASE_URL)


@app.get("/")
async def root():
    """
    Root Endpoint.
    Args: 
    Returns: dictionary 
    """
    return {"message": "Hello World"}


@app.get("/questions/{item_reference}")
async def get_item(item_reference: str, organization_id: int = Query(..., description="ID of the item bank"),
                   tags: List[str] = Query(
                       None, description="Tags for the item")):
    learnosity_tags: List[LearnosityTag] = []
    if tags is not None:
        for tag in tags:
            tag_type, tag_value = tag.split(":")
            learnosity_tags.append(LearnosityTag(type=tag_type, name=tag_value))

    return await learnosity_svc.get_item(item_reference, organization_id, learnosity_tags)


@app.post("/questions")
async def create_item(question_create_request: Question):
    return await learnosity_svc.create_item(question_create_request, settings.ORGANIZATION_ID)
