from django.urls import path
from .views import CreateTaskView, UpdateTaskView, DestroyTaskView


app_name = 'api'

urlpatterns = [
    path("api/v1/task/create/", CreateTaskView.as_view(), name="create"),
    path("api/v1/task/update/<int:pk>", UpdateTaskView.as_view(), name="update"),
    path("api/v1/task/destroy/<int:pk>", DestroyTaskView.as_view(), name="update"),
]