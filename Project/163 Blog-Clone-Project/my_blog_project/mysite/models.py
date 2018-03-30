from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    auther = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date =  models.DateTimeField(blank=True,null=True)


    def publish_date(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments():
        return self.comments.filter(approved_comments = True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE,related_name = 'comments')
    auther = models.CharField(max_length=30)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    approved_comment = models.BooleanField(default = False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
