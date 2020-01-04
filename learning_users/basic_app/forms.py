from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    '''
    Mata() is simply an inner class of django allows you to create to define metadata.
    Metadata is depends on whether you are creating models or forms.
    For forms the Meta class defines the model and fields which you are attaching to the form.
    '''
    class Meta:
        '''
        Meta class is telling django that the form should be connect to the User model.
        And the fields we want th show up are username, email and password.
        '''
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
