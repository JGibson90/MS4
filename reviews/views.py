from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm

# Create your views here.


def reviews(request):
    """A view to show all reviews"""

    reviews = Review.objects.all()
    template = "reviews/reviews.html"
    context = {
        "reviews": reviews,
    }

    return render(request, template, context)


@login_required
def add_review(request):
    """Add a review to a product"""

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added review!")
            return redirect(reverse("home"))
        else:
            messages.error(
                request, "Failed to add review. Please ensure the form is valid."
            )
    else:
        form = ReviewForm()

    template = "reviews/add_review.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """Edit a product review"""
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated review!")
            return redirect(reverse("product_detail", args=[review.product.id]))
        else:
            messages.error(
                request, "Failed to update review. Please ensure the form is valid."
            )
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f"You are editing your review for {review.product.name}")

    template = "reviews/edit_review.html"
    context = {
        "form": form,
        "review": review.product,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """Delete a review that has already been submitted"""
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, "Review deleted!")
    return redirect(reverse("product_detail", args=[review.product.id]))
