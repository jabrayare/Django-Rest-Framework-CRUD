from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Tasks

@api_view(['GET'])
def getTask(request):
  tasks = Tasks.objects.all();
  serializer = TaskSerializer(tasks, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def getTaskDetail(request, pk):
  task = Tasks.objects.get(id=pk)
  serializer = TaskSerializer(task, many=False)
  return Response(serializer.data)


@api_view(['POST'])
def CreateTask(request):
  serializer = TaskSerializer(data = request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@api_view(['POST'])
def UpdateTask(request, pk):
  task = Tasks.objects.get(id=pk)
  serializer = TaskSerializer(instance=task, data=request.data)
  if serializer.is_valid():
    serializer.save()
    print('Data: ',request.data)
  return Response(serializer.data)


@api_view(['DELETE'])
def DeleteTask(request, pk):
  task = Tasks.objects.get(id=pk)
  task.delete()
  return Response('Item Deleted')



