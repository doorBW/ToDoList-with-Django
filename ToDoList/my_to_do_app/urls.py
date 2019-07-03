# my_to_do_app > urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createTodo/', views.createTodo, name='createTodo'),
    path('doneTodo/', views.doneTodo, name='doneTodo')
]
