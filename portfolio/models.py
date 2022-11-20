from django.db import models
import uuid

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=32)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Project(models.Model):
    CATEGORY_CHOICES = (
        ('Music', 'Music'),
        ('Software Engineering', 'Software Engineering'),
    )
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=32)
    skills = models.ManyToManyField(Skill)
    link = models.URLField()
    thumbnail = models.ImageField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f'{self.email}'