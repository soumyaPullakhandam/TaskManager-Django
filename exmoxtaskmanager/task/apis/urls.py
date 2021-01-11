from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TaskList, TaskUpdate, ReportsList

urlpatterns = [
    path('task', TaskList.as_view(), name='task-list'),
    path('task/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('reports', ReportsList.as_view(), name='reports-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
