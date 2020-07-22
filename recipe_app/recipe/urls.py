from django.urls import path
from .views import index, add_meal
urlpatterns = [
    path('', index, name='index'),
    path("add_meal", add_meal, name='add_meal')
    
]
