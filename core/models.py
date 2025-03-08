from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.TextField()
    update_at = models.DateTimeField(auto_now_add=True)  # Stores in UTC by default

    def push(self): 
        return timezone.localtime(self.update_at)  

    def __str__(self):
        return self.title
