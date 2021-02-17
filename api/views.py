from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
	  'List':'/tast-list/',
	  'Detail View:':'/task-detail/<str:pk>/',
	  'Create':'/task-create/',
	  'Update':'/task-update/<str:pk>/',
	  'Delete':'/task-delete/<str:pk>/',
	}
	
	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all()
	serializer = TaskSerializer(tasks, many = True)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(pk = pk)
	serializer = TaskSerializer(tasks , many = False)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status =status.HTTP_200_OK)
	else:
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def taskUpdate(request, pk):
	tasks = Task.objects.get(pk = pk)
	serializer = TaskSerializer(instance= tasks, data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status = status.HTTP_200_OK)
	else:
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
		
@api_view(['GET', 'DELETE'])
def taskDelete(request, pk):
	tasks = Task.objects.get(pk = pk)
	tasks.delete()
	return Response(status = status.HTTP_204_NO_CONTENT)


		

