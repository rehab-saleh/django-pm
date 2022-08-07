from django import forms
from . import models

attes = {'class': 'form-control'}


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'description']
        widgets = {
            'category' : forms.Select(attrs=attes),
            'title' :forms.TextInput(attrs=attes),
            'description' : forms.Textarea(attrs=attes)
       }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'status']
        widgets = {
            'category' :  forms.Select(attrs=attes),
            'title' : forms.TextInput(attrs=attes),
            'status' : forms.Select(attrs=attes)
      }