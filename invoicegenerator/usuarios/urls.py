from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('perfil/', views.perfil, name="perfil"),
    path('logout/', views.deslogar, name="logout"),
    path('address', views.address, name='address'),
    path('addressregister', views.addressregister, name='addressregister'),
    path('address_save', views.address_save, name='address_save')

]