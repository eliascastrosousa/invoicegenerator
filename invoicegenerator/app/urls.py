from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', companylist, name='companylist'),
    path('companylist', companylist, name='companylist'),
    path('companyregister', companyregister, name='companyregister'),
    path('company_save', company_save, name='company_save')
    
]
