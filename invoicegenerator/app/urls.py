from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', companylist, name='companylist'),
    path('companylist', companylist, name='companylist'),
    path('companyregister', companyregister, name='companyregister'),
    path('company_save', company_save, name='company_save'),
    path('companydetails/<int:id>', companydetails, name='companydetails'),
    path('invoicecreate/<int:id>', invoicecreate, name='invoicecreate'),
    path('invoice_save/', invoice_save, name='invoice_save'),
    path('invoicelist/', invoicelist, name='invoicelist'),
    path('invoicedetails/<int:id>', invoicedetails, name='invoicedetails'),
    path('invoicesearch', invoicesearch, name='invoicesearch')


    
    
]
