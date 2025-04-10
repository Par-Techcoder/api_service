from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'authors'
        ordering = ['name']

    def __str__(self):
        return self.name