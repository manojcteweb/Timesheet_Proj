from pydantic import BaseModel, Field
from bson import ObjectId

class Customer(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    name: str
    email: str
    phone: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}