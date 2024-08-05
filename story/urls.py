from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:story_id>/", views.show, name="show"),
    path("<int:story_id>/<int:chapter_num>", views.show, name="show"),
    path("add", views.addstory, name="addstory"),
    path("poststory", views.poststory, name="poststory"),
    path("edit/<int:story_id>", views.editstory, name="editstory"),
]
