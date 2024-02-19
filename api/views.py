from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TaskSerializer
from .models import Task


class TestAPIView(APIView):
    def get(self, request):
        return Response({'msg': 'It works somehow'},
                        status=status.HTTP_200_OK)


class CreateTaskView(generics.CreateAPIView):
    """
    Представление для создания экземпляра модели Задача
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class UpdateTaskView(generics.UpdateAPIView):
    """
    Представление для изменения экземпляра модели Задача
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class DestroyTaskView(generics.DestroyAPIView):
    """
    Представление для удаления экземпляра модели Задача
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

