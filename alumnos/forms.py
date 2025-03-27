from .models import Alumno
from django import forms

class alumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'edad', 'matricula', 'email']

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese nombre del alumno'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese apellido del alumno'
                }
            ),
            'edad': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese nombre de la categoria'
                }
            ),
            'matricula': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese nombre de la categoria'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Ingrese nombre de la categoria'
                }
            )

        }

        labels = {
            'nombre': 'Nombre del usuario',
            'apellido': 'Apellido del usuario'
        }
