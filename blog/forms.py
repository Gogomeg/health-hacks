from .models import Comment
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Image
from djrichtextfield.widgets import RichTextWidget
from .models import HealthHack


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


class HackForm(forms.ModelForm):
    """Form to create a health hack"""

    class Meta:
        model = HealthHack
        fields = [
            "title",
            "description",
            "content",
            "image",
            "image_alt",
            "hack_type",
        ]

        content = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Health Hack Title",
            "description": "Description",
            "content": "Health Hack content",
            "image": "Health hack Image",
            "image_alt": "Describe Image",
            "hack_type": "Health Hack Type",
        }
