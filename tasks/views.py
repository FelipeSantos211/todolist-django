from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Task

# 🔹 Login
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect("home")  # Redireciona após login
        else:
            messages.error(request, "Usuário ou senha incorretos.")

    return render(request, "auth/login.html")

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)  # Filtra tarefas do usuário logado
    return render(request, "tasks/home.html", {"tasks": tasks})

# 🔹 Logout
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect("login")

# 🔹 Registro de usuário
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def user_register(request):
    if request.user.is_authenticated:
        return redirect("task_list")  # Redireciona usuários logados para a lista de tarefas

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        if password != password_confirm:
            messages.error(request, "As senhas não coincidem.")
            return render(request, "auth/register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe.")
            return render(request, "auth/register.html")

        try:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, "Cadastro realizado! Faça login.")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"Erro ao criar usuário: {str(e)}")

    return render(request, "auth/register.html")


# 🔹 Listar tarefas do usuário autenticado
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "tasks/task_list.html", {"tasks": tasks})

# 🔹 Criar uma nova tarefa (associada ao usuário logado)
@login_required
def create_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if not title:
            messages.error(request, "Tarefa vazia!")
            return redirect("create_task")
        Task.objects.create(user=request.user, title=title)
        messages.error(request, "Tarefa adicionada com sucesso!")
        return redirect("task_list")

    return render(request, "tasks/create_task.html")

# 🔹 Editar uma tarefa existente (somente do usuário autenticado)
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        task.title = request.POST.get("title")
        if not task.title:
            messages.error(request, "Tarefa vazia!")
            return redirect("edit_task", task_id=task_id)
        task.completed = request.POST.get("completed") == "on"
        task.save()
        messages.success(request, "Tarefa atualizada!")
        return redirect("task_list")

    return render(request, "tasks/edit_task.html", {"task": task})

# 🔹 Excluir uma tarefa (somente do usuário autenticado)
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    messages.success(request, "Tarefa excluída!")
    return redirect("task_list")

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')  # Redireciona de volta para a lista de tarefas
