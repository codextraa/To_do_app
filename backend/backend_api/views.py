from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core_db.models import Todo
from .filters import TodoFilter
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """Todo ViewSet"""

    permission_classes = [AllowAny]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TodoFilter
    http_method_names = ["get", "post", "patch", "delete"]

    @action(detail=True, methods=["POST"], url_path="complete")
    def complete(self, request, pk):
        """Marks a To-Do item as complete"""
        todo = get_object_or_404(Todo, id=pk)
        todo.completed = True
        todo.completed_at = now()
        todo.save()
        return Response(TodoSerializer(todo).data, status=200)

    @action(detail=True, methods=["POST"], url_path="incomplete")
    def incomplete(self, request, pk):
        """Marks a To-Do item as incomplete"""
        todo = get_object_or_404(Todo, id=pk)
        todo.completed = False
        todo.completed_at = None
        todo.save()
        return Response(TodoSerializer(todo).data, status=200)
