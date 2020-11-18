from django.db import models 
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Habit(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='habits')
    daily_target = models.IntegerField(blank=True, null=True)
    #verb = models.CharField(max_length = 20)
    noun = models.CharField(max_length = 20)
   

    
  
    


class Record(models.Model):
    date_completed = models.DateField()
    habit = models.ForeignKey(to=Habit, on_delete=models.CASCADE, related_name="records")
    number = models.IntegerField()
    
    
    class Meta:
        unique_together = [ 
            "habit",
            "date_completed",
        ]
    




