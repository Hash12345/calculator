from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path("register/", register_page, name="register"),
    path("accounts/login/", login_page, name="login"),
    path("logout/", logout_page, name="logout"),
    path("calculator/", calculator_page, name="calculator"),
    path("history/", history_page, name="history"),
    path("profile/", profile_update_page, name="profile"),
]