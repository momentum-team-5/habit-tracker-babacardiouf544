from django import forms
from core.models import Habit #Record


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [

            "name",
            "daily_target",
            #"verb", 
            #"noun", 
        ]

# class RecordForm(forms.ModelForm):
#     class Meta:
#         model = Record
#         fields = [        
#              "date_completed",
#              "number"
#              #"habit",
#              # 
#        ]
    