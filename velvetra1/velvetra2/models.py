import uuid
from django.db import models

class Designer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=50, default="active")
    password = models.CharField(max_length=255)
    avatar_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DesignProject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    # Store designer_id as a plain string (UUID string) so frontend can set it directly
    designer_id = models.CharField(max_length=255, blank=True, null=True)
    designer_name = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=100, blank=True)
    fabric_type = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=50, default="draft")
    design_images = models.JSONField(default=list)
    final_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
