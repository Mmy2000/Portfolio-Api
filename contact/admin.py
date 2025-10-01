from django.contrib import admin
from .models import Contact
from unfold.admin import ModelAdmin

# Register your models here.

@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ("id", "first_name","last_name", "email", "subject")
    search_fields = ("first_name","last_name", "email", "subject", "message")
    ordering = ("-id",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("first_name","last_name", "email"),  # grouped in one row
                    "subject",
                    "message",
                )
            },
        ),
    )
