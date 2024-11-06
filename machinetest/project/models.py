from django.db import models
from client.models import Client
from authentication.models import User

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    users = models.ManyToManyField(User, related_name='assigned_user')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "project_details"
