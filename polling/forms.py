from django import forms
from .models import Poll


class PostForm(forms.ModelForm):
    score = forms.IntegerField(
        label="Poll Score", required=False, initial=0
    )  # Add this line to include the score field in the form

    class Meta:
        model = Poll
        fields = ["title", "text", "score"]
