from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import HealthHack
from .models import Comment
from django import forms
from .models import Image
from .models import Comment
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# Apply summernote to specific fields.


class SomeForm(forms.Form):
    # instead of forms.Textarea
    foo = forms.CharField(widget=SummernoteWidget())


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
