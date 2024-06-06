from django.urls import path
from .views import (
    list_view,
    detail_view,
    stub_view,
    PostListView,
    PostDetailView,
    add_post,
)

urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
    path("add/", add_post, name="add_post"),
    # path('', list_view, name="blog_index"),
    # path('blogs/<int:blog_id>/', stub_view, name="blog_detail")
]
