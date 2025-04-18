from django.urls import path
from .views import (
    user_login, user_logout, user_register, 
    task_list, create_task, edit_task, delete_task,home,complete_task
)

urlpatterns = [
    # 🔹 Autenticação
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", user_register, name="register"),
    path('', home, name='home'),  # Rota para a home

    # 🔹 Tarefas
    path("", task_list, name="task_list"),  # Página inicial (lista de tarefas)
    path("task/create/", create_task, name="create_task"),
    path("task/edit/<int:task_id>/", edit_task, name="edit_task"),
    path("task/delete/<int:task_id>/", delete_task, name="delete_task"),
    path('task/complete/<int:task_id>/', complete_task, name='complete_task'),
]
