from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone


class Task(models.Model):
    """
        Model for Task
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', verbose_name="Created by")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', verbose_name="Assign to")
    title = models.CharField(blank=False, null=False, max_length=30)
    description = models.TextField(blank=True, null=True)
    points = models.IntegerField(blank=False, null=False)
    completed = models.IntegerField(choices=((1, 'True'), (2, "False")), default=2)
    created_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

