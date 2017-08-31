from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='',
               widget = forms.TextInput(attrs={'placeholder':'Usuario'}))
    password = forms.CharField(max_length=20, 
               widget= forms.PasswordInput(attrs={'placeholder':'Contraseña'}),label='')
