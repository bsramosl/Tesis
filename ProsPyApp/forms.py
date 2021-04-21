from builtins import property
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *


class UsuarioForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Nombre', max_length=140, required=True, )
    last_name = forms.CharField(label='Apellido', max_length=140, required=False,
                                )
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'controls', 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'controls', 'placeholder': 'Contraseña'}))

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


class ContraseñaForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UsuForm(ModelForm):
    first_name = forms.CharField(max_length=140, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=140, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=True)
    is_superuser = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_superuser'
        )

    @property
    def is_staff(self):
        return self.is_superuser


class TipoReactorForm(forms.ModelForm):
    descripcion = forms.CharField(label='Descripcion:',widget=forms.TextInput(attrs={'class': 'form-sma form-sma-titu', 'float': 'left'}))
    especificaciontecnica = forms.CharField(label='Especificacion:',widget=forms.TextInput(attrs={'class': 'form-sma form-sma-titu', 'float': 'left'}))
    tiporeactor = forms.CharField(label='Tipo:',widget=forms.TextInput(attrs={'class': 'form-sma form-sma-titu', 'float': 'left'}))

    class Meta:
        model = TipoReactor
        fields = '__all__'



class OrganismoForm(forms.ModelForm):
    nombrecientifico = forms.CharField(label='Nombre Cient:',widget=forms.TextInput(attrs={'class': 'form-sma form-sma-titu', 'float': 'left'}))
    genero = forms.CharField(label='Genero:',widget=forms.TextInput(attrs={'class': 'form-sma form-sma-titu', 'float': 'left'}))

    class Meta:
        model = Organismo
        fields = '__all__'


class ReactorForm(forms.ModelForm):

    class Meta:
        model = Reactor
        fields = '__all__'