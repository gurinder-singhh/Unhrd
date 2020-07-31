from storyhome.models import Friends
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = User    
        fields = ['first_name','last_name','username','email']

class FriendsListForm(forms.ModelForm):
    #MultipleChoiceField()
    class Meta:
        model = Friends
        fields = ['users','current_user']
        blank = True
        widgets = {
            'users': forms.CheckboxSelectMultiple(),
        }