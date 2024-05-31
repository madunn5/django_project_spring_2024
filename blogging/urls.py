from django.urls import path
from blogging.views import list_view, detail_view, stub_view, PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name="blog_index"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="blog_detail"),
    # path('', list_view, name="blog_index"),
    # path('blogs/<int:blog_id>/', stub_view, name="blog_detail")
]
