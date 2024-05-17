from django.shortcuts import render
from django.http import Http404
from blogging.models import Post


def list_view(request):
    context = {'blogs': Post.objects.all()}
    return render(request, 'blogging/list.html', context)


def detail_view(request, blog_id):
    try:
        blog = Post.objects.get(pk=blog_id)
    except Post.DoesNotExist:
        raise Http404

    context = {'blog': blog}
    return render(request, 'blogging/detail.html', context)