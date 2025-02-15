from django.db import models

class ChatResponse(models.Model):
    content = models.TextField()
    category = models.CharField(max_length=100)
    has_artifact = models.BooleanField(default=False)
    artifact_type = models.CharField(max_length=50, null=True, blank=True)
    artifact_content = models.TextField(null=True, blank=True)
