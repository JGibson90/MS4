from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    """ A model for site admin to add a blog post """
    blog_title = models.CharField(max_length=80, null=True, blank=True)
    blog_body = models.TextField(null=True, blank=True, default="")
    blog_by = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.blog_title
