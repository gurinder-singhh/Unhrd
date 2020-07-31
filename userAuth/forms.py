from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserRegistration
from django.core.exceptions import ValidationError

#Custom User Login Form
class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your Username'}))

    password = forms.CharField(widget=forms.PasswordInput(
    attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password here',
    }
))

#Custom User Signup Form
class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password',
            'class':'form-control'
    }))
    class Meta:
            model = User
            fields = ['username','email','password',]

            help_texts = {
            'username': None,
            'email': None,
        }

            widgets = {
            'password': forms.PasswordInput(attrs={'placeholder':'password',
            'class':'form-control'}),
            'email': forms.EmailInput(attrs={'required':True,
                'placeholder':'Email',
                'class':'form-control'}),
            'username': forms.TextInput(attrs={'placeholder':'Username',
            'class':'form-control'})
        }

    def save(self, commit=True):
        #   Save the provided password in hashed format
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        print(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('confirm_password')

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("The two password fields must match.")
        return cleaned_data


# def password_validator(value):
#     if self.cleaned_data["password"] == value:
#         return value
#     else:
#         raise ValidationError("Passwords are not mataching")






