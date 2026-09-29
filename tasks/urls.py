from django.urls import path
from .views import register, login_view, logout_view
from .views import task_list, create_task

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("tasks/", task_list, name="task_list"),
    path("tasks/create/", create_task, name="create_task"),
]