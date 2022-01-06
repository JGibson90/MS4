from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Coupon(models.Model):
    code = models.CharField(max_length=20)
    amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.code
