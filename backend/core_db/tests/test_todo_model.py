from django.test import TestCase
from django.utils import timezone

from core_db.models import Todo


class TodoModelTest(TestCase):
    def setUp(self):
        """Set up initial data for all test methods"""
        self.todo = Todo.objects.create(title="Test Todo", completed=False)

    def test_todo_creation(self):
        """Test basic todo creation and attributes"""
        todo = self.todo
        self.assertTrue(isinstance(todo, Todo))
        self.assertEqual(todo.title, "Test Todo")
        self.assertFalse(todo.completed)
        self.assertIsNotNone(todo.created_at)
        self.assertIsNone(todo.completed_at)

    def test_string_representation(self):
        """Test the string representation of the Todo"""
        todo = self.todo
        self.assertEqual(str(todo), "Test Todo")

    def test_title_max_length(self):
        """Test that title respects max_length constraint"""
        # Create a title that's exactly 255 characters
        long_title = "a" * 255
        todo = Todo.objects.create(title=long_title)
        self.assertEqual(len(todo.title), 255)

    def test_completed_default_value(self):
        """Test that completed defaults to False"""
        todo = Todo.objects.create(title="New Todo")
        self.assertFalse(todo.completed)

    def test_created_at_auto_now_add(self):
        """Test that created_at is automatically set"""
        todo = Todo.objects.create(title="Time Test")
        self.assertIsNotNone(todo.created_at)
        self.assertTrue(timezone.now() >= todo.created_at)

    def test_completed_at_null_by_default(self):
        """Test that completed_at is null by default"""
        todo = Todo.objects.create(title="Null Test")
        self.assertIsNone(todo.completed_at)

    def test_completed_todo(self):
        """Test todo with completed status and completed_at timestamp"""
        todo = Todo.objects.create(
            title="Completed Todo", completed=True, completed_at=timezone.now()
        )
        self.assertTrue(todo.completed)
        self.assertIsNotNone(todo.completed_at)

    def test_ordering_by_created_at(self):
        """Test that todos can be ordered by creation time"""
        Todo.objects.create(title="First")
        Todo.objects.create(title="Second")
        todos = Todo.objects.all()
        self.assertEqual(todos[0].title, "Test Todo")  # From setUp
        self.assertEqual(todos[1].title, "First")
        self.assertEqual(todos[2].title, "Second")
        self.assertTrue(
            todos[0].created_at <= todos[1].created_at <= todos[2].created_at
        )


if __name__ == "__main__":
    import unittest

    unittest.main()
