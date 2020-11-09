from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Record, Habit
from core.forms import HabitForm, RecordForm


# Create your views here.

#list many Models

def habit_list(request):
    habits = Habit.objects.all() 
    
    return render(request, "core/habit_list.html", {"habits": habits})


#show detail
@login_required
def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    
    return render(request, "core/habit_detai.html", {"habit": habit})


#create
@login_required
def habit_create(request):
    if request.method == "GET":
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect("habit", pk=habit.pk)
        
    return render(request, "core/habit_create.html", {"form": form})


#update
@login_required
def habit_update(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == "GET":
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(instance=habit, data=request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect("habit", pk=habit.pk)
    
    return render(request, "core/habit_update.html", {"habit": habit, "form": form})


#delete
@login_required
def habit_delete(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == "POST":
        habit.delete()
        return redirect("habit-list")

    return render(request, "core/habit_delete.html", {"habit": habit}) 

#create a record
@login_required
def create_record(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)

    if request.method == "GET":
        form = RecordForm()
   
    else: 
        form = RecordForm(data=request.POST)

        if form.is_valid():
            record = form.save(commit=False)
            record.habit = habit
            record.save()
            return redirect(to="habit_list")
    
    return render(request, "core/create_record.html", {"form": form, "habit": habit})










