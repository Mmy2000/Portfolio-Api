from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify 
from taggit.managers import TaggableManager


# Create your models here.
class Projects(models.Model):
    auther = models.ForeignKey(User, related_name="project_auther",verbose_name=('Project Auther'), on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name=('Project Title'))
    image = models.ImageField(("Project Image"),upload_to='projects/')
    cover_description = models.TextField(("Short Description"),max_length=100000)
    description = models.TextField(("Description"),max_length=100000)
    categoryproject = models.ForeignKey(
        "CategoryProject",
        related_name="project_category",
        verbose_name=("Project Category"),
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(null=True,blank=True)
    url = models.CharField(null=True,blank=True, max_length=50)
    github = models.CharField(null=True,blank=True, max_length=50)
    client = models.CharField(null=True,blank=True, max_length=50)
    tags = TaggableManager(blank=True)
    status = models.CharField(null=True, blank=True, max_length=50)
    duration = models.CharField(null=True, blank=True, max_length=50)
    team_size = models.CharField(null=True, blank=True, max_length=50)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(("created_at"), default=timezone.now)
    updated_at = models.DateTimeField(("updated_at"), auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Projects,self).save(*args,**kwargs)

    def __str__(self):
        return self.title


class CategoryProject(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = ("Category Project")
        verbose_name_plural = ("Category Projects")

    def __str__(self):
        return self.name

class ImageProject(models.Model):
    project = models.ForeignKey(Projects,related_name='project_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projectimages/')

    class Meta:
        verbose_name = ("Image Project")
        verbose_name_plural = ("Image Projects")
        
    def __str__(self):
        return str(self.project)
