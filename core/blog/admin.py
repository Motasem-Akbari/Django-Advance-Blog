from django.contrib import admin
from .models import Post, Category

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "title",
        "status",
        "category",
        "updaterate",
        "published_date",
    )
    list_filter = ("status", "category", "author")
    search_fields = ("title", "content")
    ordering = ("-published_date",)
    date_hierarchy = "published_date"
    fields = (
        "author",
        "title",
        "content",
        "image",
        "category",
        "status",
        "published_date",
    )
    readonly_fields = ("created_date", "updated_date")


admin.site.register(Post)
admin.site.register(Category)
