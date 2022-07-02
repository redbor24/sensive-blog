from django.contrib import admin
from blog.models import Post, Tag, Comment

LIST_PER_PAGE = 20


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'wrapped_text', 'slug', 'image', 'published_at',)
    raw_id_fields = ('likes', 'tags', )
    readonly_fields = ['published_at']
    list_per_page = LIST_PER_PAGE
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('text', 'post', 'author', 'published_at')
    list_display = ('author', 'post', 'text', 'published_at')
    raw_id_fields = ('post', 'author')
    readonly_fields = ['published_at']
    list_per_page = LIST_PER_PAGE
    pass


admin.site.register(Tag)
