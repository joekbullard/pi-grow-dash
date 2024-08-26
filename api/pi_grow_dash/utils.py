import logging
from ninja.responses import Response
from ninja.errors import ValidationError


logger = logging.getLogger(__name__)

def custom_validation_error_handler(request, exc: ValidationError):
    # Log the raw request body
    logger.error(f"Validation Error: Raw Request Body: {request.body.decode('utf-8')}")

    # Log the request headers
    logger.error(f"Validation Error: Request Headers: {request.headers}")

    # Log the validation errors
    logger.error(f"Validation Errors: {exc.errors}")

    return Response({"detail": exc.errors}, status=422)