from django.db import models 
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Habit(models.Model):
    name = models.CharField(max_length=250)
    #daily_target = models.FloatField()
    daily_target = models.IntegerField(blank=True, null=True)
    #verb = models.CharField(max_length = 20)
    #noun = models.CharField(max_length = 20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')


class Record(models.Model):
    date_completed = models.DateField()
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="records")
    text = models.TextField(blank=True)
    




