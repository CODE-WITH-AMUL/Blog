from django.db import models
from django.utils import timezone
import os
from django.core.exceptions import ValidationError  # Import ValidationError

class Blog(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def push(self): 
        return timezone.localtime(self.updated_at)

    def __str__(self):
        return self.title


# PDF Uploading Model
class Pdf(models.Model):
    file_pdf = models.FileField(upload_to='Files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        allowed_extensions = ['.pdf', '.doc', '.docx']
        ext = os.path.splitext(self.file_pdf.name)[1]
        if ext.lower() not in allowed_extensions:
            raise ValidationError("Invalid file type. Only PDF and DOC files are allowed.")

    def __str__(self):
        return f"{self.file_pdf.name}"
