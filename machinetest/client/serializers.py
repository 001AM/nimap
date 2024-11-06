from rest_framework import serializers
from client.models import Client

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = '__all__'

    def get_created_by(self, obj):
        return f"{obj.created_by.first_name} {obj.created_by.last_name}"
