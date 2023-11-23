from django.db import models


class Profile(models.Model):
    bio = models.TextField()

    def __str__(self):
        return "Profile"


class Project(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True)
    key_features = models.TextField(null=True)
    technical_stack = models.TextField(null=True)
    role_and_contribution = models.TextField(null=True)
    challenges_solutions = models.TextField(null=True)
    future_plans = models.TextField(null=True)
    web_link = models.URLField(blank=True)
    git_repo_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)  # Optional: for project screenshots

    def __str__(self):
        return self.title


