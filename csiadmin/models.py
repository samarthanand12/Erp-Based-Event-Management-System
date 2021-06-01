from django.db import models
from datetime import datetime
# Create your models here.
class Assignedtask(models.Model):
    checkername=models.CharField(max_length=200)
    filelink=models.CharField(max_length=1000)
    teamid=models.IntegerField(primary_key= True)
    date=models.DateTimeField(default=datetime.now)

class Userdata(models.Model):
    Decision=models.IntegerField()
    Reason=models.TextField(max_length=1000)
    Username=models.CharField(max_length=200)
    Id=models.IntegerField(primary_key= True)
    flink = models.CharField(max_length=1000,default="")
    date = models.DateTimeField(default=datetime.now)