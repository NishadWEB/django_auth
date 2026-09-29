from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Task

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect("login")

    return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect("task_list")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    return render(
        request,
        "task_list.html",
        {"tasks": tasks}
    )

@login_required
def create_task(request):
    if request.method == "POST":

        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            user=request.user
        )

        return redirect("task_list")

    return render(request, "create_task.html")