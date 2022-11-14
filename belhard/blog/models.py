from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    name = models.CharField(max_length=32)
    body = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('post', {'post_slug': self.slug})

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    # name = models.CharField(max_length=64)
    # email = models.EmailField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=512)
    recomment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text


class Newsletter(models.Model):
    email = models.EmailField(max_length=64)

    def __str__(self):
        return self.email
