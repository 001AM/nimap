from rest_framework import serializers
from client.models import Client

class ClientSerailzier(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
