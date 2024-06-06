from django.shortcuts import render
from django.http import Http404
from .models import Poll
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm


class PollListView(ListView):
    model = Poll
    template_name = "polling/list.html"


class PollDetailView(DetailView):
    model = Poll
    template_name = "polling/detail.html"

    def post(self, request, *args, **kwargs):
        poll = self.get_object()

        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

        context = {"object": poll}
        return render(request, "polling/detail.html", context)


@login_required
def add_poll(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("poll_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blogging/add_post.html", {"form": form})


def list_view(request):
    context = {"polls": Poll.objects.all()}
    return render(request, "polling/list.html", context)


def detail_view(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404

    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

    context = {"poll": poll}
    return render(request, "polling/detail.html", context)
