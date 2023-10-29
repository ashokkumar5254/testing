from django.db import models

# Create your models here.
class coordinates_model(models.Model):
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    def __str__(self):
        return self.lat
