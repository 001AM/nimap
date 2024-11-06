
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from client.models import Client
from client.serializers import ClientSerailzier

class ClientDetails(APIView):
    def get(self,request):
        try:
            client_id = request.GET.get('id',None)
            if client_id:
                client_instance = Client.objects.filter(id=client_id)
            else:
                client_instance = Client.objects.all()
            client_serializer  = ClientSerailzier(client_instance,many=True)
            if len(client_serializer.data) > 0:
                return JsonResponse({'response':client_serializer.data}, status=200)
            else:
                return JsonResponse({'response':"No Data available"}, status=200)
        except Exception as e:
            return JsonResponse({'error':str(e)}, status=500)

    def post(self,request):
        try:
            user = request.user
            client_name = request.POST.get('client_name')
            client_instance = Client.objects.create(client_name=client_name,created_by=user)
            return JsonResponse({'response':"Created Successfully"}, status=201)
        except Exception as e:
            return JsonResponse({'error':str(e)}, status=500)

    def put(self,request):
        try:
            client_id = request.GET.get('id')
            client_name = request.POST.get('client_name')
            client_instance = Client.objects.get(id=client_id)
            client_instance.client_name = client_name
            client_instance.save()
            return JsonResponse({'response':"Updated Successfully"}, status=201)
        except Exception as e:
            return JsonResponse({'error':str(e)}, status=500)

    def delete(self,request):
        try:
            client_id = request.GET.get('id')
            client_instance = Client.objects.get(id=client_id)
            client_instance.delete()
            return JsonResponse({'response':"Delete Successfully"}, status=204)
        except Exception as e:
            return JsonResponse({'error':"No Client available with this id"}, status=500)
