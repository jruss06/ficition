from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from story.models import Story, Chapter

def profile(request):
    story_list = Story.objects.filter(user_id=request.user.id)
    context = {
        "user": request.user,
        "story_list": story_list
    }
    return render(request, "author/index.html", context)

def viewauthor(request, author_id):
    story_list = Story.objects.filter(user_id=author_id)
    context = {
         "story_list": story_list
    }
    return render(request, "author/viewauthor.html", context)
