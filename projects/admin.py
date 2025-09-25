from django import forms
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from unfold.admin import ModelAdmin
from taggit.forms import TagField
from .models import Projects, CategoryProject, ImageProject


class ProjectsAdminForm(forms.ModelForm):
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
        model = Projects
        fields = "__all__"


@admin.register(Projects)
class ProjectsAdmin(SummernoteModelAdmin, ModelAdmin):
    form = ProjectsAdminForm
    summernote_fields = ("description", )

    list_display = ("title", "auther", "categoryproject", "created_at", "updated_at")
    list_filter = ("categoryproject", "created_at", "tags")
    search_fields = ("title", "client", "tags__name", "auther__username")
    ordering = ("-created_at",)

    readonly_fields = ("created_at", "updated_at")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ["categoryproject", "auther"]

    # ✅ Unfold form layout
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("title", "slug"),  # grouped in one row
                    ("auther", "categoryproject"),
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
                "classes": ("tab",),  # ✅ shows as tab
            },
        ),
        (
            "Extra",
            {
                "fields": (("url", "client","github"),),
                "classes": ("collapse",),  # collapsible
            },
        ),
        (
            "Timestamps",
            {
                "fields": (("created_at", "updated_at"),),
                "classes": ("collapse",),
            },
        ),
    )


@admin.register(CategoryProject)
class CategoryProjectAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(ImageProject)
class ImageProjectAdmin(ModelAdmin):
    list_display = ("project", "image")
    search_fields = ("project__title",)
    autocomplete_fields = ["project"]
