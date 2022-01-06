from django.urls import path
from . import views

urlpatterns = [
    path("add/<int:blog_id>/", views.add_blog, name="add_blog"),
    path("edit/<int:blog_id>/", views.edit_blog, name="edit_blog"),
    path("delete/<int:blog_id>/", views.delete_blog, name="delete_blog"),
]
