# PersonalPortfolioApp/models.py
from django.db import models


class Profile(models.Model):
    bio = models.TextField()

    def __str__(self):
        return "Profile"


class GitRepository(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=100, default='Git Repository')

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True)
    key_features = models.TextField(null=True)
    technical_stack = models.TextField(null=True)
    role_and_contribution = models.TextField(null=True)
    challenges_solutions = models.TextField(null=True)
    future_plans = models.TextField(null=True)
    web_link = models.URLField(blank=True)
    git_repo_links = models.ManyToManyField(GitRepository, blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/', default='default_image.jpg')

    def __str__(self):
        return f"{self.project.title} - Image"

