from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Post, Comment
from django.db.models.functions import Substr

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Post Content'), {"fields": ("title", "text")}),
        (_("Related user"), {"fields": ("user", )}),
        (_("Publication time"), {"fields": ("if_edited", 'edited_at')})
    )
    list_display = (
        'title',
        'user__username',
        'user__age',
        'pub_date',

    )
    search_fields = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Comment text'), {"fields": ('content',)}),
        (_("Related Post"), {"fields": ("Post",)}),
        (_("Related User"), {"fields": ("user",)}),
    )
    list_display = (
        'get_post_title',
        'get_short_content',
        'user__username',
        'user__age',
        'pub_date',
        'parent',
    )
    search_fields = ('short_comment',)

    def get_short_content(self, obj):
        return ' '.join(obj.content.split()[:10]) \
            + ('...' if len(obj.content.split()) > 10 else '')

    def get_search_results(self, request, queryset, search_term):
        queryset = queryset.annotate(
            short_comment=Substr('content', 1, 50)
        )
        return super().get_search_results(request, queryset, search_term)

    def get_post_title(self, obj):
        return obj.Post.title
    get_post_title.short_description = 'Post Title'

