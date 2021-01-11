from django.urls import path
from .views import home_view, task_list, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', home_view, name='home_view'),
    path('<int:pk>', task_list, name='task_list'),
    path('update/<int:pk>', TaskUpdate.as_view(), name='TaskUpdate'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='TaskDelete'),
    path('add', TaskCreate.as_view(), name='TaskCreate'),
]