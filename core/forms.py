from django import forms
from core.models import Habit, Record


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [

            "name",
            "daily_target",           
            "noun", 
            #"verb",
        
            
        ]

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
             "number",        
             "date_completed",
                           
       ]
    