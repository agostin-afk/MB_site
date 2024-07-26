from typing import Any
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import  Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title', 'is_published', 'created_by'
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'excerpt', 'content',
    list_per_page = 50
    list_filter = 'is_published',
    list_editable = 'is_published',
    ordering = '-id',
    readonly_fields = 'created_at', 'updated_at', 'updated_by', 'created_by', 'link',
    prepopulated_fields = {
        "slug": ('title',),
    }
    # autocomplete_fields = 'tags', 'category',

    def link(self, obj):
        if not obj.pk: 
            return '-'

        url_do_post = obj.get_absolute_url()
        safe_link = mark_safe(f'<a target="_blank" href= "{url_do_post}">Ver Post</a>')
        return safe_link

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
        obj.save()
