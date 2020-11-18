from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Habit, Record
from core.forms import HabitForm, RecordForm


# Create your views here.


#list many Models
def habit_list(request):
    habits = request.user.habits.all() 
    
    return render(request, "core/habit_list.html", {"habits": habits})

#habit detail
def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    records = habit.records.all()    

    return render(request, "core/habit_detail.html", {"records": records, "habit": habit})
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
            return redirect("habit_list")
        
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
            return redirect("habit_list")
    
    return render(request, "core/habit_update.html", {"habit": habit, "form": form})


#delete
@login_required
def habit_delete(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == "POST":
        habit.delete()
        return redirect("habit_list")

    return render(request, "core/habit_delete.html", {"habit": habit}) 



# #create a record list
# @login_required
# def record_update(request, record_pk):
#     record = get_object_or_404(Record.objects.filter(habit__user=request.user), pk=record_pk)
#     if request.method == "GET":
#         form = RecordForm(instance=record)
#     else:
#         form = RecordForm(data=request.POST)
#         if form.is_valid():
#             record = record.save()
#             return redirect("record_detail", pk=record.pk)
#     return render(request, "core/record_update.html", {"record": record, "form": form})


# #create a record
@login_required
def record_create(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)

    if request.method == "GET":
        form = RecordForm()
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.habit = habit
            record.save()
            return redirect("habit_detail", pk=habit.pk)
    return render(request, "core/record_create.html", {"form": form})

# #delete a record

# @login_required
# def record_delete(request, record_pk):
#     record = get_object_or_404(Record.objects.filter(habit__user=request.user), pk=record_pk)
#     record.delete()

#     return redirect(to="habit_detail", pk = record.habit )










