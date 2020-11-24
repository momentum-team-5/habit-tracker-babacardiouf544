from django.urls import path
from api import views as api_views


urlpatterns = [
    path("habit/", api_views.HabitListView.as_view()),
    path("habit/<int:pk>/", api_views.HabitDetailView.as_view()),
    path("record/", api_views.RecordCreateView.as_view()),
]