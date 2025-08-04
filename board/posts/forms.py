from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', 'image')
        widgets = {
            'text': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
        }
        labels = {
            'text': 'Text',
            'group': 'Group',
            'image': 'Image',
        }
        help_texts = {
            'text': 'Text',
            'group': 'Group to which the post belongs',
            'image': 'Choose an image to upload',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].empty_label = 'Choose a group'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        help_texts = {
            'text': 'Add a comment:',
        }
