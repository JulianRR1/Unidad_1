from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth import authenticate
import re
from django.core.exceptions import ValidationError



class CustomUserCreationForm(UserCreationForm):

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("El correo es obligatorio.")
        
        if not re.match(r"^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$", email):
            raise forms.ValidationError("El correo debe pertenecer al dominio @utez.edu.mx.")
        
        return email

    def clean_control_number(self):
        control_number = self.cleaned_data.get("control_number")
        
        if not control_number:
            raise forms.ValidationError("La matrícula es obligatoria.")

        if not re.match(r"^\d{5}[a-zA-Z]{2}\d{3}$", control_number):
            raise forms.ValidationError("La matrícula debe ser alfanumérica y de 10 caracteres.")
        
        return control_number

    def clean_tel(self):
        tel = self.cleaned_data.get("tel")
        
        if not tel:
            raise forms.ValidationError("El teléfono es obligatorio.")

        if not re.match(r"^[0-9]{10}$", tel):
            raise forms.ValidationError("El teléfono debe contener exactamente 10 dígitos numéricos.")
        
        return tel

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if not password1 or not password2:
            raise forms.ValidationError("Ambas contraseñas son obligatorias.")

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        # Validar el formato de la contraseña
        if not re.match(r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$", password1):
            raise forms.ValidationError(
                "La contraseña debe tener al menos 8 caracteres, incluir una letra mayúscula, un número y un carácter especial (!@#$%^&*)."
            )

        return password2

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        name = cleaned_data.get("name")
        surname = cleaned_data.get("surname")
        control_number = cleaned_data.get("control_number")
        age = cleaned_data.get("age")
        tel = cleaned_data.get("tel")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        return cleaned_data

    password1 = forms.CharField(
        label='Contraseña',
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico',
                'required': True,
                'pattern': '^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?]).{8,}$',
                'title': 'Ingresa contraseña',

            }
        )
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico',
                'required': True,
                'pattern': '^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?]).{8,}$',
                'title': 'Confirma Contraseña',
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = [
            'email', 'name', 'surname', 'control_number', 'age', 'tel',
            'password1', 'password2'
        ]

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo electrónico',
                    'required': True,
                    'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
                    'title': 'Ingresa correo de UTEZ',
                    'minlength': '2'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre usuario',
                    'required': True,
                    'pattern': '^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,}$',
                    'title': 'Ingresa nombre de usuario',
                    'minlength': '2'
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido del usuario',
                    'required': True,
                    'pattern': '^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,}$',
                    'title': 'Ingresa apellido de usuario',
                    'minlength': '2'
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Matricula del usuario',
                    'required': True,
                    'pattern': '^\d{5}[a-zA-Z]{2}\d{3}$',
                    'title': 'Ingresa matricula de usuario',
                    'minlength': '2'
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Edad usuario',
                    'required': True,
                    'pattern': '^(1[0-9]|[2-9][0-9]|100)$',
                    'title': 'Ingresa la edad de usuario',
                    'minlength': '2'
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Telefono usuario',
                    'required': True,
                    'pattern': '^\d{10}$',
                    'title': 'Ingresa telefono de ususario',
                    'minlength': '2'
                }
            ),
        }

        
    


class CustomUserLoginForm(AuthenticationForm):
    username  = forms.CharField(
        label="Email", 
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'})
    )
    password = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password) 
            if not user:
                raise forms.ValidationError("Usuario o contraseña incorrectos.")

        return cleaned_data
    ##pass
 