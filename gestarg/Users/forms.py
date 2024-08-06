from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User  # Asegúrate de importar el modelo User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Correo Electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}  # Limpia los mensajes de ayuda predeterminados
class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    # No obligatorios
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = [
            'email',
            'password1',
            'password2',
            'last_name',
            'first_name'
        ]
        help_texts = {k:"" for k in fields}
