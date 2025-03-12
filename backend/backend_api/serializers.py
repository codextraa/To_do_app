from rest_framework import serializers
from django.utils.timezone import now
from core_db.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        read_only_fields = ("id", "created_at")

    def update(self, instance, validated_data):
        validated_data["created_at"] = now()

        return super().update(instance, validated_data)
