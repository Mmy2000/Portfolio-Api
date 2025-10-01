from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify 


class Post(models.Model):
    auther = models.ForeignKey(User, related_name="post_auther",verbose_name=('auther'), on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name=('title'))
    tags = TaggableManager(("tags"))
    image = models.ImageField(("image"),upload_to='post/')
    description = models.TextField(("description"),max_length=100000)
    cover_description = models.TextField(("short description"),max_length=100000)
    slug = models.SlugField(null=True,blank=True)
    category = models.ForeignKey('PostCategory',related_name='post_category',verbose_name=('category'),on_delete=models.CASCADE ,null=True,blank=True)
    created_at = models.DateTimeField( ("created_at"),default=timezone.now)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")
    
    def __str__(self):
        return self.title
    

class PostImages(models.Model):
    post = models.ForeignKey(Post, related_name='post_image', on_delete=models.CASCADE)
    image = models.ImageField( upload_to='postImages')

    class Meta:
        verbose_name = ("Post Image")
        verbose_name_plural = ("Post Images")

    def __str__(self):
        return str(self.post.title)
    
class PostCategory(models.Model):
    name = models.CharField(null=True,blank=True, max_length=50)

    class Meta:
        verbose_name = ("Post Category")
        verbose_name_plural = ("Post Categories")

    def __str__(self):
        return self.name