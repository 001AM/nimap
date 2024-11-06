from django.db import models
from authentication.models import User

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')

    def __str__(self):
        return self.client_name
    class Meta:
        db_table = "client_details"
