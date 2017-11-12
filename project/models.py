from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Project(models.Model):
    projectname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Slider(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    index = models.IntegerField(default=1)
    image = models.ImageField(upload_to='slider_image')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

    def __str__(self):
        return "%s" % self.name


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name.replace(' ', '_')

    class Meta:
        verbose_name = "Portfolio Category"
        verbose_name_plural = "Portfolio Categories"


class PortfolioItems(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to='portfolio_images', default='portfolio_images/image-1.jpg')
    category = models.ForeignKey(PortfolioCategory, blank=True, null=True, default=None)
    url = models.URLField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return self.category.replace(' ', '_')

    class Meta:
        verbose_name = "Portfolio Item"
        verbose_name_plural = "Portfolio Items"


class ServiceItems(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    icon = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Service Item"
        verbose_name_plural = "Service Items"


class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=64, default=None)
    subject = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"


class PostCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Post Category"
        verbose_name_plural = "Posts Categories"


class BlogPosts(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=True)
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to='blog_images')
    category = models.ForeignKey(PostCategory, blank=True, null=True, default=None)
    tag = models.CharField(max_length=32, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "$s" % self.id

    def get_absolute_url(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"


class PostComment(models.Model):
    post = models.ForeignKey(BlogPosts, related_name='comments', blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField()
    web_site = models.URLField(max_length=64, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Post Comment"
        verbose_name_plural = "Posts Comments"