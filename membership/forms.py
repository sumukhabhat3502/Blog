from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from base.models import userProfile


class SignUp(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=225, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=225, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
    # Django provides username and password by default so we are styling it in the below format

    def __init__(self, *args, **kwargs):
        super(SignUp, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfile(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=225, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=225, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(
        max_length=225, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}))
    # last_login=forms.CharField(max_length=225,widget=forms.TextInput(attrs={'class':'form-control'}))
    # is_superuser=forms.CharField(max_length=225,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
   # is_staff=forms.CharField(max_length=225,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    # is_active=forms.CharField(max_length=225,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    # date_joined=forms.CharField(max_length=225,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfilePage(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ('bio_data', 'profile_pic', 'Instagram_url',
                  'linkedin_url', 'website_url', 'Twitter_url')
        widgets = {
            # form-control is the name of the class in bootstrap forms i.e, why it is being used here
            'bio_data': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'This is Title '}),
            # 'profile_pic': forms.TextInput(attrs={'class':'form-control'}),
            'Instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'Twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
