from rest_framework import serializers

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
      Serializer for Task model.
    """
    username = serializers.CharField(source='user', read_only=True)
    author_name = serializers.CharField(source='author', read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class ReportsSerializer(serializers.Serializer):
    """
        Serializer for Report model.
    """
    user = serializers.CharField()
    total_users = serializers.IntegerField()
    pending_tasks = serializers.IntegerField()
    completed_tasks = serializers.IntegerField()
    pending_points = serializers.IntegerField()
    completed_points = serializers.IntegerField()

    class Meta:
        fields = ['user', 'total_users', 'pending_total', 'completed_total', 'pending_points', 'completed_points']
