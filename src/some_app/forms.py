from django import forms
from some_app.models import Student


class SomeForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'age')
