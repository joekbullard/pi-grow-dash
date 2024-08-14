from django.db import models

# {
#   "nickname": "weather-test", 
#   "model": "grow",
#   "uid": "e6614c775b8c4035", 
#   "timestamp": "2022-09-04T10:40:24Z", 
#   "readings": {
#     "temperature": 27.57,   // will change depending on board model
#     "humidity": 49.33, 
#     "pressure": 996.22, 
#     "light": 0.41, 
#     "moisture_1": 0.0, 
#     "moisture_2": 0.0, 
#     "moisture_3": 0.0, 
#     "voltage": 4.954
#   }
# }

class GrowReading(models.Model):
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