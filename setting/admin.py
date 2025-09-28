from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Info, Roles
# Register your models here.

@admin.register(Info)
class InfoAdmin(ModelAdmin):
    list_display = ("site_name", "f_name", "l_name", "email")
    search_fields = ("site_name", "f_name", "l_name", "email")
    ordering = ("-id",)
    filter_horizontal = ("role",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("site_name", "email"),  # grouped in one row
                    ("f_name", "l_name"),
                    "description",
                    "role",
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
            "Social Links",
            {
                "fields": (
                    "fb_link",
                    "twitter_link",
                    "instagram_link",
                    "githup_link",
                    "linkedin_link",
                ),
                "classes": ("tab",),  # ✅ shows as tab
            },
        ),
    )

@admin.register(Roles)
class RolesAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("name",),  # grouped in one row
                )
            },
        ),
    )