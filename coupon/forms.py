from django import forms
from .models import Coupon


class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = (
            "code",
        )

    # def __init__(self, *args, **kwargs):
    #     """add placeholders and classes"""

    #     super().__init__(*args, **kwargs)
    #     placeholders = {
    #         "coupon_code": "Coupon Code",

    #     }

    #     for field in self.fields:
    #         placeholder = placeholders[field]
    #         self.fields[field].widget.attrs["placeholder"] = placeholder
    #         self.fields[field].widget.attrs["class"] = "stripe-style-input"
    #         self.fields[field].label = False
