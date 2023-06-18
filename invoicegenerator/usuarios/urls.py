from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.perfil, name="perfil"),
    path('perfil/', views.perfil, name="perfil"),
    path('additionaldata', views.additionaldata, name='additionaldata'),
    path('additionaldata_register', views.additionaldata_register, name='additionaldata_register'),
    path('additionaldata_save', views.additionaldata_save, name='additionaldata_save')

]