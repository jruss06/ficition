from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Story, Chapter


def index(request):
    story_list = Story.objects.order_by("-update_date")[:5]
    context = {
        "story_list": story_list,
    }
    return render(request, "story/index.html", context)

def show(request, story_id, chapter_num=1):
    story = get_object_or_404(Story, pk=story_id)
    chapter = get_object_or_404(Chapter, story_id=story_id, order=chapter_num)
    chapter_list = Chapter.objects.filter(story_id = story_id)
    return render(request, "story/show.html", {"story": story, "chapter": chapter, "chapter_list": chapter_list})

def addstory(request):
    return render(request, "story/addstory.html")

def poststory(request):
    story = Story.objects.create(
            title=request.POST["title"],
            summary=request.POST["summary"],
            user=request.user)
    Chapter.objects.create(
            title=request.POST["chaptertitle"],
            body=request.POST["body"],
            story=story,
            order=1,
            user=request.user)
    return HttpResponseRedirect(reverse("profile"))

def addchapter(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    return render(request, "story/addchapter.html", {"story": story})

def postchapter(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    Chapter.objects.create(
            title=request.POST["chaptertitle"],
            body=request.POST["body"],
            story=story,
            order=request.POST["order"],
            user=request.user)
    return HttpResponseRedirect(reverse("profile"))

def editstory(request, story_id):
    story = Story.objects.get(pk=story_id)
    chapters = Chapter.objects.filter(story_id=story_id)
    context = {
        "story": story,
        "chapters": chapters,
    }
    return render(request, "story/edit.html", context)

def postedit(request, story_id):
    story = Story.objects.get(pk=story_id)
    story.title=request.POST["title"]
    story.summary=request.POST["summary"]
    story.save()
    return HttpResponseRedirect(reverse("profile"))

def editchapter(request, story_id, chapter_id):
    story = Story.objects.get(pk=story_id)
    chapter = Chapter.objects.get(pk=chapter_id)
    context = {
        "story": story,
        "chapter": chapter,
    }
    return render(request, "story/editchapter.html", context)

def posteditChapter (request, story_id, chapter_id):
    story = Story.objects.get(pk=story_id)
    chapter = Chapter.objects.get(pk=chapter_id)
    chapter.title=request.POST["chaptertitle"]
    chapter.body=request.POST["body"]
    chapter.order=request.POST["order"]
    chapter.save()
    story.save()
    return HttpResponseRedirect(reverse("profile"))
