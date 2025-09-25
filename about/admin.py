from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from unfold.admin import ModelAdmin

from .models import (
    About,
    Education,
    Summary,
    ProfessionalExperience,
    EXP,
    MySkills,
    CategorySkills,
    Language,
)


# ---- Admin classes ----
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin, ModelAdmin):
    summernote_fields = ("about",)
    list_display = ("username", "phone_number", "email", "views")
    search_fields = ("username", "email")
    list_filter = ("degree", "age")
    fieldsets = (
        (
            "Personal Info",
            {"fields": ("user", "username", "phone_number", "email", "date_of_birth")},
        ),
        ("Profile Details", {"fields": ("headline", "address", "image", "resume")}),
        ("Additional Info", {"fields": ("about", "age", "degree", "views")}),
    )


@admin.register(Education)
class EducationAdmin(SummernoteModelAdmin, ModelAdmin):
    summernote_fields = ("description",)
    list_display = ("user", "year", "title", "university")
    search_fields = ("title", "university")


@admin.register(Summary)
class SummaryAdmin(SummernoteModelAdmin, ModelAdmin):
    summernote_fields = ("description",)
    list_display = ("user", "email", "phone", "address")


@admin.register(ProfessionalExperience)
class ProfessionalExperienceAdmin(ModelAdmin):
    list_display = ("user", "year", "title", "university")


@admin.register(EXP)
class EXPAdmin(ModelAdmin):
    list_display = ("get_exp", "subject")  # ✅ use method instead of raw M2M field

    def get_exp(self, obj):
        return ", ".join([str(e) for e in obj.exp.all()])

    get_exp.short_description = "Experiences"


@admin.register(MySkills)
class MySkillsAdmin(ModelAdmin):
    list_display = ("category", "percent")


@admin.register(CategorySkills)
class CategorySkillsAdmin(ModelAdmin):
    list_display = ("name",)


@admin.register(Language)
class LanguageAdmin(ModelAdmin):
    list_display = ("name", "percent")
