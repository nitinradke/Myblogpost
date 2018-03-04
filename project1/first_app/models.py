from django.db import models

# Create your models here.
class info_table(models.Model):
    """inf_table description)"""
    rollno = models.BigIntegerField(unique = True,primary_key = True)
    name = models.CharField(max_length = 30)
    Age = models.IntegerField()
    Semester = models.IntegerField()
    Section = models.CharField(max_length = 1)


    def __self__(self):
        return str(self.rollno)
