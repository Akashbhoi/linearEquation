# forms.py
from django import forms


class EquationForm(forms.Form):
    equation1 = forms.CharField(label='Equation 1', max_length=100)
    equation2 = forms.CharField(label='Equation 2', max_length=100)
