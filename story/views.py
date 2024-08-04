from django.shortcuts import get_object_or_404, render
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
    return render(request, "story/show.html", {"story": story, "chapter": chapter})
