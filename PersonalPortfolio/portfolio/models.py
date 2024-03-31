# portfolio/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'portfolio'
