from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .forms import PostForm


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blogging/list.html"

    def get_queryset(self):
        return Post.objects.exclude(published_date__exact=None).order_by(
            "-published_date"
        )


class PostDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"

    def get_queryset(self):
        # Exclude posts with no published date and order by published date
        return Post.objects.exclude(published_date__exact=None).order_by(
            "-published_date"
        )

    def get_context_data(self, **kwargs):
        # This will allow for the extra detail should we need it, currently there is nothing being added here
        context = super().get_context_data(**kwargs)
        return context


@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("blog_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blogging/add_post.html", {"form": form})


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by("-published_date")
    context = {"posts": posts}
    return render(request, "blogging/list.html", context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    context = {"post": post}
    return render(request, "blogging/detail.html", context)


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args: \n"
        body += "\n".join(["\t%s" % i for i in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")
