from rest_framework import generics, permissions
from django.db.models import Sum

from exmoxtaskmanager.restconf.permission import IsAdminOrReadOnly, IsAdminOrReadUpdateOnly
from ..models import Task
from django.contrib.auth.models import User
from .serializers import TaskSerializer, ReportsSerializer


class TaskList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Task.objects.all()
        else:
            queryset = Task.objects.filter(user=self.request.user)

        completed = self.request.query_params.get('completed')

        if completed:
            queryset = queryset.filter(completed=completed)

        return queryset


class TaskUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadUpdateOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ReportsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReportsSerializer

    def get_queryset(self):
        user_type = self.request.user.is_staff
        if not user_type:
            user_task = Task.objects.filter(user=self.request.user)
            total_users = 0
        else:
            user_task = Task.objects.all()
            total_users = User.objects.filter(is_staff=False).count()
        pending_points = user_task.filter(completed=2).aggregate(Sum('points'))
        completed_points = user_task.filter(completed=1).aggregate(Sum('points'))

        queryset = [{"user": self.request.user,
                     "total_users": total_users,
                     "pending_tasks": user_task.filter(completed=2).count(),
                     "completed_tasks": user_task.filter(completed=1).count(),
                     "pending_points": pending_points.get('points__sum'),
                     "completed_points": completed_points.get('points__sum')}]
        return queryset
