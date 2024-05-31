from django.shortcuts import render
from django.http import Http404, HttpResponse
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostListView(ListView):
    model = Post.objects.exclude(published_date__exact=None)
    queryset = Post.objects.order_by("-published_date")
    context_object_name = "posts"
    template_name = 'blogging/list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'
    queryset = Post.objects.order_by("-published_date")

    def get_queryset(self):
        # Exclude posts with no published date and order by published_date
        return Post.objects.exclude(published_date__exact=None).order_by("-published_date")

    def get_context_data(self, **kwargs):
        # Add any additional context if needed
        context = super().get_context_data(**kwargs)
        return context


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blogging/list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    context = {'post': post}
    return render(request, 'blogging/detail.html', context)


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args: \n"
        body += "\n".join(["\t%s" % i for i in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")
