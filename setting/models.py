from django.db import models

# Create your models here.


class Info(models.Model):
    site_name = models.CharField(max_length=50)
    f_name = models.CharField("First Name",max_length=50)
    l_name = models.CharField("Last Name",max_length=50)
    description = models.TextField(max_length=1000)
    email = models.EmailField(max_length=254, null=True, blank=True)
    image = models.ImageField(upload_to="users/", null=True, blank=True)
    role = models.ManyToManyField("setting.Roles", related_name="info_roles")
    fb_link = models.URLField(max_length=200)
    twitter_link = models.URLField(max_length=200)
    instagram_link = models.URLField(max_length=200)
    githup_link = models.URLField(null=True, blank=True, max_length=200)
    linkedin_link = models.URLField(null=True, blank=True, max_length=200)

    class Meta:
        verbose_name = "Info"
        verbose_name_plural = "Info"

    def __str__(self):
        return self.site_name


class Roles(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.name