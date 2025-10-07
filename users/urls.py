from django.urls import path

from users.views import show_login, show_logout, show_register

app_name = "users"

urlpatterns = [
    path("register/", show_register, name="show_register"),
    path("login/", show_login, name="show_login"),
    path("logout/", show_logout, name="show_logout"),
]
