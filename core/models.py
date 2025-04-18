from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='resumes/')  # Required
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    skills = models.CharField(max_length=1000, blank=True)
    resume_file = models.FileField(upload_to='resumes/', null=True, blank=True)  # Optional field

    def __str__(self):
        return self.name or "Resume"
