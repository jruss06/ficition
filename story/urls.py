from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:story_id>", views.show, name="show"),
    path("<int:story_id>/<int:chapter_num>", views.show, name="show"),
    path("add", views.addstory, name="addstory"),
    path("add/<int:story_id>/chapter", views.addchapter, name="addchapter"),
    path("poststory", views.poststory, name="poststory"),
    path("postedit/<int:story_id>", views.postedit, name="postedit"),
    path("posteditchapter/<int:story_id>/<int:chapter_id>", views.posteditChapter, name="posteditchapter"),
    path("postchapter/<int:story_id>", views.postchapter, name="postchapter"),
    path("edit/<int:story_id>", views.editstory, name="editstory"),
    path("edit/<int:story_id>/chapter/<int:chapter_id>", views.editchapter, name="editchapter"),
]
