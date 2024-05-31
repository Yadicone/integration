from django import forms
from .models import Employé
class EmployéForm(forms.ModelForm):
    class Meta:
        model=Employé
        fields='__all__'