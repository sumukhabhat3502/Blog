# To create input forms

from django import forms
from django.contrib.auth import get_user
from .models import Comment, Post, Category

choice = Category.objects.all().values_list(
    'name', 'name')  # For Dropdown in category section
choice_list = []

for item in choice:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'author', 'category',
                  'body', 'header_image', 'para')
        widgets = {
            # form-control is the name of the class in bootstrap forms i.e, why it is being used here
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title '}),
            'tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a Tag '}),
            'author': forms.TextInput(attrs={'id': 'author', 'class': 'form-control', 'value': '', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Choose a Category '}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the blog'}),
            # 'para':forms.Textarea(attrs={'class':'form-control'})
            'para': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Give a snippet'})
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'body', 'para')
        widgets = {
            # form-control is the name of the class in bootstrap forms i.e, why it is being used here
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title '}),
            'tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a Tag '}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the body'}),
            'para': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Give a snippet'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            # form-control is the name of the class in bootstrap forms i.e, why it is being used here
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'aut'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
