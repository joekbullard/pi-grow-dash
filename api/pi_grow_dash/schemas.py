from ninja import Schema
import datetime
from typing import List


class ReadingsSchema(Schema):
    temperature: float
    humidity: float
    pressure: float
    luminance: float
    moisture_a: float
    moisture_b: float
    moisture_c: float


class ReadingsOutSchema(ReadingsSchema):
    timestamp: datetime.datetime


class ReadingIn(Schema):
    nickname: str
    uid: str
    timestamp: datetime.datetime
    readings: ReadingsSchema | None


class BoardOut(Schema):
    user: int
    nickname: str
    uid: str
    readings: List[ReadingsOutSchema] = None
