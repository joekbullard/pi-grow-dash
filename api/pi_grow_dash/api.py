from .models import Board, Reading
from ninja import NinjaAPI
from .schemas import BoardOut, ReadingIn
from ninja.errors import ValidationError
from ninja.security import HttpBasicAuth
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from ninja.errors import HttpError
from .utils import custom_validation_error_handler


api = NinjaAPI(csrf=True)

User = get_user_model()


class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password):
        try:
            user = User.objects.get(username=username)
            # Use Django's password hashing to check the password
            if check_password(password, user.password):
                return user
            else:
                raise HttpError(401, "Incorrect password")
        except User.DoesNotExist:
            raise HttpError(401, "User not found")


basic_auth = BasicAuth()

# need to add usernane validator

api.add_exception_handler(ValidationError, custom_validation_error_handler)


@api.get("/boards/{board_id}", response=BoardOut)
def list_boards(request, board_id: int):
    board = Board.objects.get(id=board_id)
    readings = board.readings.all()

    data = {
        "user": board.user.id,
        "nickname": board.nickname,
        "uid": board.uid,
        "readings": readings,
    }

    return data


@api.post("/readings", auth=basic_auth)
def create_new_reading(request, payload: ReadingIn):
    try:
        obj, created = Board.objects.get_or_create(
            user=request.auth, uid=payload.uid, nickname=payload.nickname
        )

        reading = Reading.objects.create(
            board=obj, timestamp=payload.timestamp, **payload.readings.dict()
        )

        return {"id": reading.id}

    except ValidationError as e:
        return {"error": "Invalid data", "details": e.errors()}, 422
