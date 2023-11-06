from django import forms
from .models import Post, Comment, Tag, movieComment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'content', 'thumb_image', 'movieAd']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']


class MovieTagForm(forms.ModelForm):
    class Meta:
        model = movieComment
        fields = ['movieAd', 'image','message']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        
        
        
        
        
