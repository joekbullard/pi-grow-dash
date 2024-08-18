from django.db import models
from django.conf import settings

# Two options for the model, either flat like this


class GrowReading(models.Model):
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE
    # )
    nickname = models.CharField(max_length=40)
    uid = models.CharField(max_length=16)
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    luminance = models.FloatField()
    moisture_a = models.FloatField()
    moisture_b = models.FloatField()
    moisture_c = models.FloatField()


# or maybe like this? Use a nested model with a Board model that relates to a Reading model 1:N


class Board(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40)
    uid = models.CharField(max_length=16)


class Reading(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    luminance = models.FloatField()
    moisture_a = models.FloatField()
    moisture_b = models.FloatField()
    moisture_c = models.FloatField()
