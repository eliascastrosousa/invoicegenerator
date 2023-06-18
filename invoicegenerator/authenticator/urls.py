from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.authenticator, name="authenticator"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.deslogar, name="logout")

]