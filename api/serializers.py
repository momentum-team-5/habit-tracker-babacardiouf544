from rest_framework import serializers
from core.models import Habit, Record  


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Habit
        fields = [
            'name', 'noun', 'daily_target', 'user',
            ]


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record 
        fields = [
            'name', 'daily_target',
        ]