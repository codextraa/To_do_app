from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core_db.models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """Todo ViewSet"""

    permission_classes = [AllowAny]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=["POST"], url_path="complete")
    def complete(self, request):
        """Marks a To-Do item as complete"""
        todo_id = request.data.get("id")
        if not todo_id:
            return Response({"error": "ID is required"}, status=400)

        todo = get_object_or_404(Todo, id=todo_id)
        todo.completed = True
        todo.completed_at = now()
        todo.save()

        return Response(TodoSerializer(todo).data, status=200)
