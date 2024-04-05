from django.contrib import admin
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ["title", "counted_view", "status", "publish_date"]
    search_fields = ["title", "content"]
    list_filter = ["status"]
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
