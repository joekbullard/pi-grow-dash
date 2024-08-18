from .models import GrowReading
from ninja import NinjaAPI
from ninja import Schema
import datetime
import logging
from ninja.errors import ValidationError
from ninja.responses import Response
from typing import List

logger = logging.getLogger(__name__)

api = NinjaAPI()


class ReadingsSchema(Schema):
    temperature: float
    humidity: float
    pressure: float
    luminance: float
    moisture_a: float
    moisture_b: float
    moisture_c: float

class ReadingsOutSchema(Schema):
    timestamp: datetime.datetime
    temperature: float
    humidity: float
    pressure: float
    luminance: float
    moisture_a: float
    moisture_b: float
    moisture_c: float


class ReadingIn(Schema):
    nickname: str
    uid: str
    timestamp: datetime.datetime
    readings: ReadingsSchema | None


class ReadingOut(Schema):
    nickname: str
    uid: str
    readings: List[ReadingsOutSchema] = None
    # temperature: float
    # humidity: float
    # pressure: float
    # luminance: float
    # moisture_a: float
    # moisture_b: float
    # moisture_c: float


def custom_validation_error_handler(request, exc: ValidationError):
    # Log the raw request body
    logger.error(f"Validation Error: Raw Request Body: {request.body.decode('utf-8')}")

    # Log the request headers
    logger.error(f"Validation Error: Request Headers: {request.headers}")

    # Log the validation errors
    logger.error(f"Validation Errors: {exc.errors}")

    return Response({"detail": exc.errors}, status=422)


api.add_exception_handler(ValidationError, custom_validation_error_handler)


@api.post("/readings")
def create_reading(request, payload: ReadingIn):
    logger.info(f"Raw Request Body: {request.body.decode('utf-8')}")

    # Log the request headers
    logger.info(f"Request Headers: {request.headers}")

    # Log the parsed data
    logger.info(f"Parsed Data: {payload.dict()}")

    try:
        flattened_data = {
            "nickname": payload.nickname,
            "uid": payload.uid,
            "timestamp": payload.timestamp,
        }

        flattened_data.update(payload.readings.dict())

        reading = GrowReading.objects.create(**flattened_data)
        return {"id": reading.id}

    except ValidationError as e:
        logger.error(f"Validation Error: {e.errors()}")
        return {"error": "Invalid data", "details": e.errors()}, 422


@api.get("/readings", response=ReadingOut)
def list_readings(request):
    logger.info(f"Raw Request Body: {request.body.decode('utf-8')}")
    queryset = GrowReading.objects.all()

    try:
        reading_list = []
        for qs in queryset:
            reading = {
                'timestamp': qs.timestamp,
                "temperature": qs.temperature,
                "humidity": qs.humidity,
                "pressure": qs.pressure,
                "luminance": qs.luminance,
                "moisture_a": qs.moisture_a,
                "moisture_b": qs.moisture_b,
                "moisture_c": qs.moisture_c,
            }

            reading_list.append(reading)

        structured_data = {
            'nickname': queryset[0].nickname,
            'uid': queryset[0].uid,
            'readings': reading_list
        }

        logger.info(f'{structured_data}')
    except ValidationError as e:
        logger.error(f"Validation Error: {e.errors()}")
        return {"error": "Invalid data", "details": e.errors()}, 422

    return structured_data
