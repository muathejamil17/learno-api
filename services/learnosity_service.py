from learnosity_sdk.request import DataApi
from learnosity_sdk.utils import Uuid
from models.learnosity_models import Question


class LearnosityService:

    def __init__(self, consumer_key: str, consumer_secret: str, domain: str, questions_endpoint: str) -> None:
        self.data_api = DataApi()
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.domain = domain
        self.questions_endpoint = questions_endpoint

    async def get_item(self, item_reference: str, organization_id: int):
        security_packet = {
            "consumer_key": self.consumer_key,
            "domain": self.domain,
            "user_id": "muathe@chalktalk.com"
        }
        request_packet = {
            "activity_id": Uuid.generate(),
            "items": [item_reference],
            "organisation_id": organization_id
        }

        response = self.data_api.request(
            self.questions_endpoint,
            security_packet,
            self.consumer_secret,
            request_packet
        )
        return response.json()

    async def create_item(self, question: Question, organization_id: int):
        security_packet = {
            "consumer_key": self.consumer_key,
            "domain": self.domain,
            "user_id": "muathe@chalktalk.com"
        }
        request_packet = {
            "questions": [
                question
            ],
            "organization_id": organization_id
        }
        response = self.data_api.request(
            self.questions_endpoint,
            security_packet,
            self.consumer_secret,
            request_packet,
            "set"
        )
        return response.json()
