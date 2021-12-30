from django.db import models

# Create your models here.

TYPES_OF_PROJECT = (
    ('web', 'Web app'),
    ('mobile', 'Mobile app'),
    ('desktop', 'Desktop app'),
)


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=255)
    project_type = models.CharField(max_length=100, choices=TYPES_OF_PROJECT)
    budget_range = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
