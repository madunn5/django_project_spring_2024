from django.utils import timezone
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]

    def save(self, commit=True):
        post = super().save(commit=False)
        if not post.published_date:
            post.published_date = timezone.now()
        if commit:
            post.save()
            self.save_m2m()
        return post
