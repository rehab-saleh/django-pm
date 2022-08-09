from django import forms
from . import models
from django.utils.translation import gettext as _

attes = {'class': 'form-control'}


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'description']
        labels = {
            'category': _('Category'),
            'title': _('Title'),
            'description': _('Description'),
        }
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