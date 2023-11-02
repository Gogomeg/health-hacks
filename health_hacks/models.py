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


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class BlogsModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
