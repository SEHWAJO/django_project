from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # title = forms.CharField(max_length=50, label='제목')
    # content = forms.CharField(label='내용', widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['title', 'content']
