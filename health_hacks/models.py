from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


# Create your models here.

HACK_TYPES = (('Supplements', 'suplements'), ('Research', 'research'), ('Longevity', 'longevity'),
              ('Wellness', 'wellness'), ('Meditation',
                                         'meditation'), ('Hot cold therapy', 'hot cold therapy'),
              ('Sun therapy', 'sun therapy'), ('Diet', 'diet'), ('Exercise', 'exercise'))


class HealthHack(models.Model):
    """
    A model to create and manage health hacks
    """

    user = models.ForeignKey(
        User, related_name="hack_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    content = RichTextField(max_length=3000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="health_hacks/",
        force_format="WEBP",
        blank=False,
        null=False,)
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    hack_type = models.CharField(
        max_length=50, choices=HACK_TYPES, default="suplements")
    posted_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.title)
