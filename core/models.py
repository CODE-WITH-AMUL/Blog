from django.db import models
from django.utils import timezone
import os

class Blog(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)  # Fixed variable name

    def push(self): 
        return timezone.localtime(self.updated_at)  

    def __str__(self):
        return self.title


# PDF Uploading Model
class Pdf(models.Model):
    file_pdf = models.FileField(upload_to='Files/')  # Removed invalid 'type' argument
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        
        allowed_extensions = ['.pdf', '.doc', '.docx']  # Corrected '.dox' to '.docx'
        ext = os.path.splitext(self.file_pdf.name)[1]  # Get file extension
        if ext.lower() not in allowed_extensions:
            raise ValueError("Invalid file type. Only PDF and DOC files are allowed.")

    def __str__(self):
        return f"PDF File: {self.file_pdf.name}"  # Return file name as a string
