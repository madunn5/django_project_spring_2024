from django.contrib import admin
from .models import Poll


class PollAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "text", "score")
    search_fields = ("author", "title")
    list_filter = ("score",)


admin.site.register(Poll, PollAdmin)
