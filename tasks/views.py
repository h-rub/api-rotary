from django.http.response import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from authentication.authTokenRotary import CsrfExemptTokenAuthentication
from django.shortcuts import render
import json
# Generics views
from rest_framework import generics
from tasks.models import Task
from authentication.models import CustomUser
from tasks.serializers import TaskSerializer

from rest_framework.response import Response
from rest_framework import status

class TasksList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (CsrfExemptTokenAuthentication,)

class MyTasksList(generics.ListCreateAPIView):
    
    serializer_class = TaskSerializer
    #permission_classes = (IsAuthenticated, )
    #authentication_classes = (CsrfExemptTokenAuthentication,)

    def get_queryset(self):
        user = self.request.query_params.get('user')
        queryset = Task.objects.filter(asigned_to=user)
        return queryset

def delete_task(request, id_task):
    task = Task.objects.get(_id_task = id_task).delete()
    task_db = str(task)
    responseData = {"msg":f"Task {task_db} has been deleted"}
    return HttpResponse(json.dumps(responseData), content_type="application/json")

class CreateTask(APIView):
    def post(self, request):
        title_task = request.data['title']
        description_task = request.data['description']
        deadline = request.data['deadline']
        due_time = request.data['due_time']
        assigned_to = request.data['id_assigned_to']
        # TODO Receive user to assigned
        task_asigned_to = CustomUser.objects.get(pk=assigned_to)
        created = Task.objects.create(title = title_task, description = description_task, due_date=deadline, time_date = due_time, asigned_to=task_asigned_to)
        return Response({"msg":"Tarea recibida"}, status=status.HTTP_200_OK)