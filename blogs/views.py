from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Blog
from .forms import BlogForm


def blogs(request):
    """ A view to show the blogs """
    blogs = Blog.objects.all()
    template = "blogs/blogs.html"
    context = {
        "blogs": blogs,
    }

    return render(request, template, context)


@login_required
def add_blog(request):
    """Add a blog post"""
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blogs = form.save(commit=False)
            blogs.blog_by = request.user

            blogs.save()

            messages.success(request, "Successfully added blog post!")
            return redirect(reverse("blogs", args=[blog.id]))
        else:
            messages.error(
                request, "Failed to add blog post. Please ensure the form is valid."
            )
    else:
        form = BlogForm()

    template = "blogs/add_blog.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """Edit a blog post"""
    blogs = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blogs)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated blog post!")
            return redirect(reverse("blogs", args=[blogs]))
        else:
            messages.error(
                request, "Failed to update blog post. Please ensure the form is valid."
            )
    else:
        form = BlogForm(instance=blogs)
        messages.info(request, f"You are editing your blog post {blogs.blog_title}")

    template = "blogs/edit_blog.html"
    context = {
        "form": form,
        "blogs": blogs,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """Delete a blog post that has already been submitted"""
    blogs = get_object_or_404(Blog, pk=blog_id)
    blogs.delete()
    messages.success(request, "Blog post deleted!")
    return redirect(reverse("blogs", args=[blog.blog.id]))
