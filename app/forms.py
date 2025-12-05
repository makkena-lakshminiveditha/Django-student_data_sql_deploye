from django import forms
from app.models import student_model
class student_form(forms.ModelForm):
    class Meta:
        model = student_model
        fields = '__all__'