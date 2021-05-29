from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.db.models import Sum
from django_countries.fields import CountryField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Post(models.Model):
    objects = models.Manager()     #Our Default Manager
    published = PublishedManager() #Our Custom Model Manager

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title   =   models.CharField(max_length=100)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    slug    =   models.SlugField(max_length=120)
    likes   =   models.ManyToManyField(User, related_name='likes', blank=True)
    author  =   models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body    =   RichTextField(blank=True, null=True)
    created =   models.DateTimeField(auto_now_add=True)
    updated =   models.DateTimeField(auto_now=True)
    status  =   models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    restrict_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.id, self.slug])


@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to="images/profiles")
    bio = models.TextField()
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return "Profile of user {}".format(self.user.username)

    def get_absolute_url(self):
        return reverse('post_list')


class Images(models.Model):
    post =  models.ForeignKey(Post, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.post.title + "Image"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, related_name="replies")
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))