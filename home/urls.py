from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/get_all',GetAllTasks.as_view()),
    path('tasks/create', GetAllTasks.as_view()),
    path('tasks/update/<int:id>', GetAllTasks.as_view()),
    path('tasks/delete/<int:id>', GetAllTasks.as_view()),
]

