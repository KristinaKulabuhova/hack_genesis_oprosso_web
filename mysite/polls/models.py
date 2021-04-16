import datetime

from django.db import models
from django.utils import timezone

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    people = models.IntegerField(default=0)
    link = models.CharField(max_length=200)
    pub_date = models.DateField()

class RunTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
