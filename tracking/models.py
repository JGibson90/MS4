import uuid

from django.db import models
from checkout.models import Order

# Create your models here.


class Tracking(models.Model):
    """A model for users to track their purchases"""

    tracking_number = models.CharField(max_length=32, null=False, editable=False)

    def _generate_tracking_number(self):
        """Generate a random, unique tracking number using UUID"""
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """Override the original save method to set the tracking number if it hasn't been set already"""
        if not self.tracking_number:
            self.tracking_number = self._generate_tracking_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tracking_number
