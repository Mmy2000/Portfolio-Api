from django.contrib import admin
from .models import Post, PostImages, PostCategory
from django_summernote.admin import SummernoteModelAdmin
from unfold.admin import ModelAdmin
from taggit.forms import TagField
from django import forms


class PostAdminForm(forms.ModelForm):
    tags = TagField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "unfold-input block w-full rounded-md border border-input bg-background "
                "px-3 py-2 text-sm text-foreground focus:outline-none "
                "focus:ring-2 focus:ring-blue-400 focus:border-blue-500",
                "placeholder": "Add tags separated by commas",
            }
        ),
    )

    class Meta:
        model = Post
        fields = "__all__"

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin, ModelAdmin):
    form = PostAdminForm
    summernote_fields = ("description",)

    list_display = ("title", "auther", "category", "created_at")
    list_filter = ("category", "created_at", "tags")
    search_fields = ("title", "tags__name", "auther__username")
    ordering = ("-created_at",)

    readonly_fields = ("created_at",)
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ["category", "auther"]

    # ✅ Unfold form layout
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("title", "slug"),  # grouped in one row
                    ("auther", "category"),
                    "tags",
                )
            },
        ),
        (
            "Media",
            {
                "fields": ("image",),
            },
        ),
        (
            "Descriptions",
            {
                "fields": ("cover_description", "description"),
            },
        ),
        (
            "Dates",
            {
                "fields": (("created_at",),),
            },
        ),
    )

@admin.register(PostImages)
class PostImagesAdmin(ModelAdmin):
    list_display = ("post", "image")
    search_fields = ("post__title",)
    ordering = ("-post__created_at",)
    autocomplete_fields = ["post"]

@admin.register(PostCategory)
class PostCategoryAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)