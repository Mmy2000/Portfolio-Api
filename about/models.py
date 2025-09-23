from django.db import models
from django.contrib.auth.models import User


class About(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    headline = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="users/", null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    resume = models.FileField(upload_to="files/", max_length=100, blank=True, null=True)
    about = models.TextField(blank=True)
    age = models.IntegerField(null=True, blank=True)
    degree = models.CharField(max_length=50, blank=True, null=True)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"

    def __str__(self):
        return str(self.username)


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    university = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=100000)

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"

    def __str__(self):
        return str(self.user)


class Summary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True, max_length=100000)

    class Meta:
        verbose_name = "Summary"
        verbose_name_plural = "Summaries"

    def __str__(self):
        return str(self.user)


class ProfessionalExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    university = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Professional Experience"
        verbose_name_plural = "Professional Experiences"

    def __str__(self):
        return str(self.title)


class EXP(models.Model):
    exp = models.ForeignKey(
        ProfessionalExperience, related_name="exp", on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "EXP"
        verbose_name_plural = "EXPs"

    def __str__(self):
        return str(self.exp)

class MySkills(models.Model):
    category = models.ForeignKey('CategorySkills',related_name='skills_category',on_delete=models.CASCADE)
    percent = models.CharField(max_length=30)

    class Meta:
        verbose_name = "My Skill"
        verbose_name_plural = "My Skills"
    
    def __str__(self):
        return str(self.category)


class CategorySkills(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Category Skill"
        verbose_name_plural = "Category Skills"

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=60)
    percent = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"

    def __str__(self):
        return self.name
