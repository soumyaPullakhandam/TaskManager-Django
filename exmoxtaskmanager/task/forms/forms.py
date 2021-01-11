from django import forms
from ..models import Task
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    """
        Forms for Task
    """
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created_date', 'author']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Assign to'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'points': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Points'}),
            'completed': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Completed'}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(is_staff=False)
