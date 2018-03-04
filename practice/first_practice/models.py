from django.db import models
# Create your models here
class info(models.Model):
    """( description)"""
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

class userinfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.name
