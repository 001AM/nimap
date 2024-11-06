from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'client'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('client_details/', views.ClientDetails.as_view(), name='client_details'),
]
