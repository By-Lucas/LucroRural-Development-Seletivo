
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Opcional")
    last_name = forms.CharField(max_length=30, required=False, help_text="Opcional")
    email = forms.EmailField(max_length=120, help_text="Digite seu endereço de email")

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'idade',
            'cidade',
            'endereco',
            'contato',
            'data_nascimento',
            'imagem_perfil',
            #'data_cadastro'
        ]

    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['data_cadastro'].widget = forms.DateInput(format="%d/%m/%Y")
