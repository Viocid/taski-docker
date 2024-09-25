"""q."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """q."""

    class Meta:
        """q."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
