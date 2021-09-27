from django.db import models
from django.contrib.auth.models import User

from products.models import Product

# Create your models here.


class Review(models.Model):
    """A model for users to be able to review products they've purchased"""

    review_title = models.CharField(max_length=80, null=True, blank=True)
    review_body = models.TextField(null=True, blank=True, default="")
    review_by = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.review_title
