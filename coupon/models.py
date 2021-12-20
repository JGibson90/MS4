from django.db import models

# Create your models here.


class Coupon(models.Model):
    code = models.CharField(max_length=20)
    amount = models.FloatField()

    def __str__(self):
        return self.code
