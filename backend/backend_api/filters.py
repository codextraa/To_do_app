import django_filters
from core_db.models import Todo


class TodoFilter(django_filters.FilterSet):
    """Todo Filter"""

    title = django_filters.CharFilter(lookup_expr="icontains")
    completed = django_filters.BooleanFilter(field_name="completed")

    class Meta:
        """Initialization"""

        model = Todo
        fields = ["title", "completed"]
