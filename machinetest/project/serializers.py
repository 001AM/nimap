from rest_framework import serializers
from project.models import Project

class ProjectSerailizer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField()
    users = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_created_by(self, obj):
        return f"{obj.created_by.first_name} {obj.created_by.last_name}"

    def get_client_name(self, obj):
        return f"{obj.client.client_name}"

    def get_users(self, obj):
        return [
            {
                'id': user.id,
                'name': f'{user.first_name} {user.last_name}'
            }
            for user in obj.users.all()  # Accessing all related User objects
        ]
