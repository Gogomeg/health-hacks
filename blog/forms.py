from .models import Comment
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Image


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

# Apply summernote to specific fields.


class SomeForm(forms.Form):
    # instead of forms.Textarea
    foo = forms.CharField(widget=SummernoteWidget())


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
