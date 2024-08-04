from django.urls import path

from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path("view/<int:author_id>", views.viewauthor, name="viewauthor"),
]
