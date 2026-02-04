from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("home/", views.home, name="home_page"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("signup/", views.signup_view, name="signup"),
    path("bp/add", views.add_bp, name="add_bp"),
    path("bp/history/", views.bp_history, name="bp_history"),
]