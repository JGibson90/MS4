from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Blog
from .forms import BlogForm


@login_required
def add_blog(request):
    """Add a blog post"""
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.blog_by = request.user

            blog.save()

            messages.success(request, "Successfully added blog post!")
            return redirect(reverse("home"))
        else:
            messages.error(
                request, "Failed to add blog post. Please ensure the form is valid."
            )
    else:
        form = BlogForm()

    template = "reviews/add_blog.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """Edit a blog post"""
    blog = get_object_or_404(Blog)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated blog post!")
            return redirect(reverse("blog", args=[blog.blog.id]))
        else:
            messages.error(
                request, "Failed to update blog post. Please ensure the form is valid."
            )
    else:
        form = BlogForm(instance=blog)
        messages.info(request, "You are editing your blog post")

    template = "blog/edit_blog.html"
    context = {
        "form": form,
        "blog": blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """Delete a blog post that has already been submitted"""
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, "Blog post deleted!")
    return redirect(reverse("blog", args=[blog.blog.id]))
