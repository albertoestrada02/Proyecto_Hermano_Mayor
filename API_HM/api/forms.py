from logging import PlaceHolder
from django import forms

from .models import Church, UserT, Parameter

class UserTForm(forms.ModelForm):
    isAdmin = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    firstName = forms.CharField( label="perro", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}))

    class Meta:
        model = UserT
        fields = '__all__'


class ChurchForm(forms.ModelForm):
    
    class Meta:
        model = Church
        fields = '__all__'
        exclude = [
            'id_church',
            'id_parameter',
        ]

class ParameterForm(forms.ModelForm):
    # lastupdate = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    class Meta:
        model = Parameter
        fields = '__all__'
        exclude = [
            'ID_User',
            'lastupdate'
        ]

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    firstName = forms.CharField(max_length=40, label='Nombre: ')
    lastName = forms.CharField(max_length=50, label='Apellido: ')
    gender = forms.CharField(max_length=20, label='Género: ')
    phone = forms.CharField(max_length=255, label='Teléfono: ')
    password = forms.CharField(max_length=255, label='Password: ')
    mail = forms.CharField(max_length=50, label='Email: ')
    id_church = forms.ModelChoiceField(queryset=Church.objects.all(), label='Iglesia: ')
    isAdmin = forms.BooleanField(required=False, label='Administrador')

class Registro(forms.Form):
    username = forms.CharField(label='Username')
    firstName = forms.CharField(max_length=40, label='Nombre: ')
    lastName = forms.CharField(max_length=50, label='Apellido: ')
    gender = forms.CharField(max_length=20, label='Género: ')
    phone = forms.CharField(max_length=255, label='Teléfono: ')
    password = forms.CharField(max_length=255, label='Password: ')
    mail = forms.CharField(max_length=50, label='Email: ')
    id_church = forms.ModelChoiceField(queryset=Church.objects.all(), label='Iglesia: ')