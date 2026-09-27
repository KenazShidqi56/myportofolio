#NOTE: ubah nama 'choices' di variabel 'category'

from django.db import models

# Create your models here.
# tutorial 2...
import uuid
from django.db import models

# tutorial 4...
from django.contrib.auth.models import User

# Tutorial 3...
class Experience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    event_owner = models.CharField(blank=True, max_length=255)
    event_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(User, related_name="starred_experience", blank=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    education_level = models.CharField(blank=True, max_length=255)
    education_url = models.CharField(blank=True, max_length=255)
    education_image_url = models.CharField(blank=True, max_length=255)
    starred_by = models.ManyToManyField(User, related_name="starred_education", blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    skill_category = models.CharField(blank=True, max_length=255)
    skill_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(User, related_name="starred_skill", blank=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True)
    project_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(User, related_name="starred_project", blank=True)

    def __str__(self):
        return self.title