from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from core_db.models import Todo  # Adjust import based on your app structure
from backend_api.filters import TodoFilter  # Adjust import based on your app structure
from backend_api.serializers import (
    TodoSerializer,
)  # Adjust import based on your app structure


class TodoViewSetTest(APITestCase):
    def setUp(self):
        """Set up test data and client."""
        self.client = APIClient()
        self.todo1 = Todo.objects.create(title="Buy milk", completed=False)
        self.todo2 = Todo.objects.create(title="Walk the dog", completed=True)
        self.todo3 = Todo.objects.create(title="Buy dog food", completed=False)
        self.todo4 = Todo.objects.create(title="Clean the house", completed=True)

    def test_get_all_todos(self):
        """Test GET /todos/ - list all todos."""
        url = reverse("todo-list")  # Assumes viewset registered with 'todo' basename
        response = self.client.get(url)
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_all_todos_with_filter(self):
        """Test GET /todos/ with filters (e.g., ?title=buy&completed=false)."""
        url = reverse("todo-list")
        response = self.client.get(url, {"title": "buy", "completed": "false"})
        filtered_todos = TodoFilter(
            {"title": "buy", "completed": "false"}, queryset=Todo.objects.all()
        ).qs
        serializer = TodoSerializer(filtered_todos, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(
            len(response.data), 2
        )  # Should match "Buy milk" and "Buy dog food"

    def test_get_single_todo(self):
        """Test GET /todos/{id}/ - retrieve a single todo."""
        url = reverse("todo-detail", args=[self.todo1.id])
        response = self.client.get(url)
        serializer = TodoSerializer(self.todo1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_todo(self):
        """Test POST /todos/ - create a new todo."""
        url = reverse("todo-list")
        data = {"title": "New Todo", "completed": False}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 5)
        self.assertEqual(Todo.objects.get(id=response.data["id"]).title, "New Todo")

    def test_put_update_not_allowed(self):
        """Test PUT /todos/{id}/ - ensure PUT is not allowed."""
        url = reverse("todo-detail", args=[self.todo1.id])
        data = {"title": "Updated Todo", "completed": True}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_partial_update_todo(self):
        """Test PATCH /todos/{id}/ - partial update of a todo."""
        url = reverse("todo-detail", args=[self.todo1.id])
        data = {"title": "Partially Updated Todo"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo1.refresh_from_db()
        self.assertEqual(self.todo1.title, "Partially Updated Todo")
        self.assertFalse(self.todo1.completed)  # Should remain unchanged

    def test_delete_todo(self):
        """Test DELETE /todos/{id}/ - delete a todo."""
        url = reverse("todo-detail", args=[self.todo1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 3)
        with self.assertRaises(Todo.DoesNotExist):
            Todo.objects.get(id=self.todo1.id)

    def test_mark_todo_complete(self):
        """Test POST /todos/{id}/complete/ - mark a todo as complete."""
        url = reverse(
            "todo-complete", args=[self.todo1.id]
        )  # Assumes 'complete' action
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo1.refresh_from_db()
        self.assertTrue(self.todo1.completed)
        self.assertIsNotNone(self.todo1.completed_at)

    def test_mark_todo_incomplete(self):
        """Test POST /todos/{id}/incomplete/ - mark a todo as incomplete."""
        url = reverse(
            "todo-incomplete", args=[self.todo2.id]
        )  # Assumes 'incomplete' action
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo2.refresh_from_db()
        self.assertFalse(self.todo2.completed)
        self.assertIsNone(
            self.todo2.completed_at
        )  # Assumes incomplete resets completed_at
