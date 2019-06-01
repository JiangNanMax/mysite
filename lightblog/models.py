from django.db import models
from ckeditor.fields import RichTextField

class LightBlog(models.Model):
    content = RichTextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_time)
        
    class Meta:
        ordering = ['-created_time']