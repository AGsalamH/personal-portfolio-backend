from django.db import models

# Create your models here.

AVAILABLE_SOCIALS = (
    ('github', 'Github'),
    ('linkedin', 'Linkedin'),
    ('facebook', 'Facebook'),
    ('twitter', 'Twitter'),
    ('instagram', 'Instagram'),
    ('google', 'Google'),
    ('dev', 'Dev'),
    ('hashnode', 'Hashnode'),
    ('stackoverflow', 'Stackoverflow'),
    ('medium', 'Medium'),
    ('youtube', 'Youtube'),
    ('pinterest', 'Pinterest'),
)

GRADES = (
    ('good', 'Good'),
    ('very good', 'Very Good'),
    ('excellent', 'Excellent'),
)


class Social(models.Model):
    name = models.CharField(choices=AVAILABLE_SOCIALS, max_length=50)
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    link = models.URLField()

    def __str__(self):
        return self.name


class Resume(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    personal_picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    university = models.CharField(max_length=100)
    college = models.CharField(max_length=150)
    department = models.CharField(max_length=150, blank=True)
    overview = models.TextField(blank=True)
    grade = models.CharField(max_length=50, choices=GRADES, blank=True)
    graduated_in = models.CharField(max_length=4, blank=True)
    joined_in = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return f'{self.university} ({self.college})'

