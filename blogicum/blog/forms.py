from django import forms
from django.contrib.auth.models import User

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'location', 'pub_date', 'image']
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']