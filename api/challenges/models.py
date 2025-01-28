from django.db import models


# Create your models here.
class Challenge(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    stack = models.JSONField()
    description = models.TextField()
    snippet = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]
