from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .models import Coupon

from checkout.views import checkout
from checkout.models import Order

# Create your views here.


def get_coupon(request, code):
    """ Gets coupon code from database """
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon

    except ObjectDoesNotExist:
        messages.info(request, "This coupon does not exist")
        return redirect(checkout)


def add_coupon(request, code):
    """ Add coupon to an order """
    try:
        order = Order.objects.get(user=request.user, ordered=False)
        order.coupon = get_coupon(request, code)
        order.save()
        messages.success(request, "Successfully added coupon")
        return HttpResponse(status=200)

    except ObjectDoesNotExist:
        messages.info(request, "You do not have an active order")
        return redirect(checkout)
