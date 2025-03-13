from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import OpenApiParameter, OpenApiResponse, extend_schema
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

    @extend_schema(
        summary="List All Todos",
        description="""Retrieve a list of all todo items, optionally
                        filtered by title or completed status.""",
        parameters=[
            OpenApiParameter(
                name="title",
                description="Filter by title (case-insensitive)",
                required=False,
                type=str,
            ),
            OpenApiParameter(
                name="completed",
                description="Filter by completion status",
                required=False,
                type=bool,
            ),
        ],
        responses={
            200: TodoSerializer(many=True),
            400: OpenApiResponse(
                description="Bad Request - Invalid parameters",
                response={
                    "type": "object",
                    "properties": {
                        "errors": {
                            "type": "string",
                            "example": "Invalid filter parameters",
                        }
                    },
                },
            ),
            500: OpenApiResponse(
                description="Internal Server Error",
                response={
                    "type": "object",
                    "properties": {
                        "errors": {"type": "string", "example": "Internal Server Error"}
                    },
                },
            ),
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Get Single Todo",
        description="Retrieve details of a single todo item by ID.",
        responses={
            200: TodoSerializer,
            404: OpenApiResponse(
                description="Not Found - Todo item does not exist",
                response={
                    "type": "object",
                    "properties": {
                        "errors": {"type": "string", "example": "Todo not found"}
                    },
                },
            ),
            500: OpenApiResponse(
                description="Internal Server Error",
                response={
                    "type": "object",
                    "properties": {
                        "errors": {"type": "string", "example": "Internal Server Error"}
                    },
                },
            ),
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Create Todo",
        description="Create a new todo item.",
        request=TodoSerializer,
        responses={
            201: TodoSerializer,
            400: OpenApiResponse(
                description="Bad Request - Invalid data",
                response={
                    "type": "object",
                    "properties": {
                        "errors": {"type": "string", "example": "Invalid request data"}
                    },
                },
            ),
            500: OpenApiResponse(
                description="Internal Server Error",
                response={
                    "type": "object",
                    "properties": {
                        "errors": {"type": "string", "example": "Internal Server Error"}
                    },
                },
            ),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Partial Update Todo",
        description="""Partially update an existing
                        todo item by ID using PATCH (PUT is not supported).""",
        request=TodoSerializer,
        responses={
            200: TodoSerializer,
            400: OpenApiResponse(
                description="Bad Request - Invalid data",
                response={
                    "type": "object",
                    "properties": {
                        "errors": {"type": "string", "example": "Invalid request data"}
                    },
                },
            ),
            404: OpenApiResponse(
                description="Not Found - Todo item does not exist",
                response={
                    "type": "object",
                    "properties": {
                        "errors": {"type": "string", "example": "Todo not found"}
                    },
                },
            ),
            500: OpenApiResponse(
                description="Internal Server Error",
                response={
                    "type": "object",
                    "properties": {
                        "errors": {"type": "string", "example": "Internal Server Error"}
                    },
                },
            ),
        },
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Delete Todo",
        description="Delete a todo item by ID.",
        responses={
            204: None,
            404: OpenApiResponse(
                description="Not Found - Todo item does not exist",
                response={
                    "type": "object",
                    "properties": {
                        "errors": {"type": "string", "example": "Todo not found"}
                    },
                },
            ),
            500: OpenApiResponse(
                description="Internal Server Error",
                response={
                    "type": "object",
                    "properties": {
                        "errors": {"type": "string", "example": "Internal Server Error"}
                    },
                },
            ),
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(
        summary="Mark Todo as Complete",
        description="Mark a todo item as completed, setting completed_at to the current time.",
        request=None,
        responses={
            200: TodoSerializer,
            404: OpenApiResponse(
                description="Not Found - Todo item does not exist",
                response={
                    "type": "object",
                    "properties": {
                        "errors": {"type": "string", "example": "Todo not found"}
                    },
                },
            ),
            500: OpenApiResponse(
                description="Internal Server Error",
                response={
                    "type": "object",
                    "properties": {
                        "errors": {"type": "string", "example": "Internal Server Error"}
                    },
                },
            ),
        },
    )
    @action(detail=True, methods=["POST"], url_path="complete")
    def complete(self, request, pk):
        """Marks a To-Do item as complete"""
        todo = get_object_or_404(Todo, id=pk)
        todo.completed = True
        todo.completed_at = now()
        todo.save()
        return Response(TodoSerializer(todo).data, status=200)

    @extend_schema(
        summary="Mark Todo as Incomplete",
        description="Mark a todo item as incomplete, clearing the completed_at timestamp.",
        request=None,
        responses={
            200: TodoSerializer,
            404: OpenApiResponse(
                description="Not Found - Todo item does not exist",
                response={
                    "type": "object",
                    "properties": {
                        "errors": {"type": "string", "example": "Todo not found"}
                    },
                },
            ),
            500: OpenApiResponse(
                description="Internal Server Error",
                response={
                    "type": "object",
                    "properties": {
                        "errors": {"type": "string", "example": "Internal Server Error"}
                    },
                },
            ),
        },
    )
    @action(detail=True, methods=["POST"], url_path="incomplete")
    def incomplete(self, request, pk):
        """Marks a To-Do item as incomplete"""
        todo = get_object_or_404(Todo, id=pk)
        todo.completed = False
        todo.completed_at = None
        todo.save()
        return Response(TodoSerializer(todo).data, status=200)
