from rest_framework import serializers

from .models import Executor, Task


class ExecutorSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Исполнитель
    """
    class Meta:
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Задание
    """
    class Meta:
        model = Task
        fields = "__all__"



