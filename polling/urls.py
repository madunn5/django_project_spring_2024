from django.urls import path
from .views import list_view, detail_view, PollListView, PollDetailView, add_poll

urlpatterns = [
    path("", PollListView.as_view(), name="poll_index"),
    path("polls/<int:pk>/", PollDetailView.as_view(), name="poll_detail"),
    path("add/", add_poll, name="add_poll"),
]
