from django.db import models
from django.contrib.auth.models import User, auth
from django.http import request
from django.urls import reverse_lazy, reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    tag = models.CharField(max_length=255, default="Sanctum")
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    # If User is deleted his/her blogs will also be deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    para = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="Uncat")
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        # because author is an object
        return self.title + ' || ' + str(self.author)

    def get_absolute_url(self):  # Where the page redirects automatically if not mentioned
        # return reverse('detail', args=(str(self.id)))
        return reverse('home')


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # Where the page redirects automatically if not mentioned
        # return reverse('detail', args=(str(self.id)))
        return reverse('home')


class userProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio_data = models.TextField()
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="media/profiles/")
    Twitter_url = models.CharField(max_length=255, null=True, blank=True)
    Instagram_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):  # Where the page redirects automatically if not mentioned
        # return reverse('detail', args=(str(self.id)))
        return reverse('home')


class Comment(models.Model):
    # to associate post with comment
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    # name=models.ForeignKey(User,on_delete=models.CASCADE,auto_created=True)
    # name=models.TextField(max_length=255)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
