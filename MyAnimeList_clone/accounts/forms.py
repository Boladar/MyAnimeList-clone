from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User,UserProfile

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields=('username','email','password1','password2')

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields=('profile_picture',)