
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from client.models import Client
from authentication.models import User
from project.models import Project
from project.serializers import ProjectSerailizer

class ProjectDetails(APIView):

    def get(self,request):
        try:
            project_instance = Project.objects.filter(users=request.user)
            project_serailzier  = ProjectSerailizer(project_instance,many=True)
            if not project_serailzier:
                return JsonResponse({'response':'No Project is assigned to you'}, status=200)
            else:
                return JsonResponse({'response':project_serailzier.data}, status=200)
        except Exception as e:
            return JsonResponse({'error':str(e)}, status=500)

    def post(self,request):
        try:
            user = request.user
            client_id = request.POST.get('client_id')
            project_name = request.POST.get('project_name')
            users = eval(request.POST.get('users'))
            client_instance = Client.objects.get(id=client_id)
            project_instance = Project.objects.create(
                project_name=project_name,
                client=client_instance,
                created_by=user
            )

            # Add users to the ManyToManyField
            user_instances = User.objects.filter(id__in=users)
            project_instance.users.add(*user_instances)
            return JsonResponse({'response':"Created Successfully"}, status=201)
        except Exception as e:
            return JsonResponse({'error':str(e)}, status=500)
