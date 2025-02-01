from django.contrib import admin
from django.db import models

from .models import FAQ, FAQTranslation


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "translation_count")
    search_fields = ("question",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("New FAQ for BharatFD", {"fields": ("question", "answer")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    def translation_count(self, obj):
        return obj.translations.count()

    translation_count.short_description = "Translations"


class FAQTranslationAdmin(admin.ModelAdmin):
    list_display = (
        "faq",
        "language",
        "question",
        "answer",
    )
    search_fields = ("faq",)
    list_filter = ("created_at", "language")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "FAQ Translation",
            {"fields": ("faq", "language", "question", "answer")},
        ),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )


admin.site.register(FAQTranslation, FAQTranslationAdmin)
