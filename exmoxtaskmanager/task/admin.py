from django.contrib import admin
from .models import Task
from .forms import TaskForm


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'points', 'completed', 'author', 'created_date']
    # readonly_fields = ['author']

    list_filter = [
        ('user', admin.RelatedOnlyFieldListFilter),
        ('author', admin.RelatedOnlyFieldListFilter)
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        return TaskForm

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(TaskAdmin, self).save_model(request, obj, form, change)


admin.site.register(Task, TaskAdmin)
