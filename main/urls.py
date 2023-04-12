from django.urls import path
from . import views

urlpatterns = [
    path('',views.getAllTodos),
    path('todos/<str:id>', views.getTodoById, name='todos'),
    path('create/', views.createTodo, name='create'),
    path('update/<str:id>', views.updateTodo, name='update'),
    path('delete/<str:id>', views.deleteTodo, name='delete'),
    path('signup/', views.userSignup, name='signup'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
]