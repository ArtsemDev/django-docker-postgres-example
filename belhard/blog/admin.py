from django.contrib import admin

from .models import Post, Comment, Newsletter


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Newsletter)
class Newsletter(admin.ModelAdmin):
    pass
