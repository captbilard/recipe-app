from django.shortcuts import render
from .forms import AddMealForm
from django.shortcuts import redirect
from .models import Meals
# Create your views here.
def index(request):
    meals = Meals.objects.all()
    return render(request, 'index.html', {'meals':meals})

def add_meal(request):
    if request.method == 'POST':
        form = AddMealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddMealForm()
        context = {'add_meal_form':form}
        return render (request, 'add-meal.html', context)
        