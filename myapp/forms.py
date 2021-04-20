from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'url', 'phone']
        labels = {'name': 'Name', 'url': 'Url', 'phone': 'Phone'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'url': forms.URLInput(attrs={'class': 'form-control'}),
                   'phone': forms.NumberInput(attrs={'class': 'form-control'}),
                   }



