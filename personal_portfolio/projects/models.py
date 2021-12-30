from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=70, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=70, unique=True)

    class Meta:
        verbose_name = 'technology'
        verbose_name_plural = 'technologies'

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=250)
    overview = models.TextField(blank=True)
    technologies = models.ManyToManyField(
        'Technology', related_name='projects', blank=True)
    category = models.ForeignKey(
        'category', on_delete=models.CASCADE, blank=True, null=True)

    github = models.URLField()
    image = models.ImageField(upload_to='projects', blank=True, null=True)

    def __str__(self):
        return self.name
