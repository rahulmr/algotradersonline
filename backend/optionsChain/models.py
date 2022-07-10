from django.db import models

class LTP(models.Model):
    name = models.CharField(max_length=100)
    ltp = models.FloatField()

    def __str__(self):
        return f"{self.name} {self.ltp}"

# Create your models here.
