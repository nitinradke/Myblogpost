from django.db import models

# Create your models here
class School(models.Model):
    """Student description)"""
    name = models.CharField(max_length = 30)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=40)

    def __str__(self):
        return self.name
