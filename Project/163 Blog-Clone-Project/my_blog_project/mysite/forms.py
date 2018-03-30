from django import forms
from mysite.models import Post,Comment


class PostForm(models.ModelForm):

    class Meta:
        model = Post
        fields = ('auther','title', 'text')
    widgets = {
        'title' : forms.TextInput(attrs = {'class':'textinputclass'})
        'text' : forms.Textarea(attrs = {'class':'editable medium-editor-textarea postcontent'})
    }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('auther','text',)
    widgets = {
        'title' : forms.TextInput(attrs = {'class':'textinputclass'})
        'text' : forms.Textarea(attrs = {'class':'editable medium-editor-textarea postcontent'})
    }
