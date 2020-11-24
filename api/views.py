from core.models import Habit, Record
from api.serializers import HabitSerializer, RecordSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.exceptions import PermissionDenied

# Create your views here.


class HabitListView(ListCreateAPIView):
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            return Habit.objects.for_user(self.request.user)

        return self.request.user.habits.all()

    
class RecordCreateView(CreateAPIView):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()
# if habit isn't the one for the current user raise 403 forbidden permission denied
    def perform_create(self, serializer):
        habit = serializer.validated_data['habit']
        if habit.user != self.request.user:
            raise PermissionDenied(
                detail="Can not perform, not your habit.")
        serializer.save()
