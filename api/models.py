from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=64, unique=True)
    icon = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class ContactSubmission(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.name} <{self.email}>"