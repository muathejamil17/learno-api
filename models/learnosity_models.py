"""
Learnosity models.
"""
from pydantic import BaseModel
from typing import List, Literal


class Option(BaseModel):
    value: str
    label: str


class ValidResponse(BaseModel):
    value: List[str]
    score: int


class Validation(BaseModel):
    scoring_type: Literal["exactMatch"]
    valid_response: List[ValidResponse]


class Data(BaseModel):
    options: List[Option]
    stimulus: str
    type: Literal["mcq"]
    validation: Validation


class Question(BaseModel):
    """
       Learnosity question model.
    """
    type: Literal["mcq"]
    reference: str
    data: Data
