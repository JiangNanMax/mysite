from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class BlogType(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    readed_num = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now_add=True)

    def __str(self):
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ['-created_time']