from django.contrib.auth.models import AbstractUser
from django.db import models

class Issue(models.Model):
    issue_type=[
        ('Dried Well','Dried Well'),
        ('Leakage','Leakage'),
        ('Waterlogging','Waterlogging'),
    ]
    name = models.CharField()
    contact = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    issue_type = models.CharField(choices=issue_type)
    description = models.TextField(blank=True)
    issue_img = models.ImageField(upload_to='issue_pics/', null=True, blank=True)

class Volunteer(models.Model):
    work_area=[
        ('Field Work','Field Work'),
        ('Awareness Programs','Awareness Programs'),
        ('Tech Support','Tech Support'),
    ]
    name = models.CharField()
    contact = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    availability = models.DateField(blank=True)
    work_area = models.CharField(choices=work_area)
