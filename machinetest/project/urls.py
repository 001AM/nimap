from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'project'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('project_details/', views.ProjectDetails.as_view(), name='project_details'),

]
