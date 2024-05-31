from django.contrib import admin

from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category.post.through
    extra = 1  # makes it so one additional blank line will show on the admin page automatically
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    search_fields = ('title', 'text')
    list_filter = ('created_date', 'published_date')
    inlines = [CategoryInline]

    def get_categories(self, obj):
        return obj.get_categories()
    get_categories.short_description = 'Categories'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    exclude = ('post',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
