from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.CharField(max_length=200)
    image_url = models.URLField()
    demo_link = models.URLField(blank=True)
    source_link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('technical', 'Technical Skills'),
        ('professional', 'Professional Skills'),
    ]

    name = models.CharField(max_length=100)
    percentage = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"