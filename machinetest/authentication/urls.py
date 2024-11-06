from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login')
]
