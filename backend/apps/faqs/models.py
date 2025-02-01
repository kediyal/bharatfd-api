import asyncio
import uuid

from asgiref.sync import async_to_sync, sync_to_async
from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from googletrans import Translator


class FAQ(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.TextField(
        help_text="Question in default language (English)"
    )
    answer = RichTextField(help_text="Answer in default language (English)")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question[:50]

    def get_translated(self, lang="en"):
        try:
            translation = self.translations.get(language=lang)
            return {
                "question": translation.question,
                "answer": translation.answer,
            }
        except FAQTranslation.DoesNotExist:
            return {
                "question": self.question,
                "answer": self.answer,
            }

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"


class FAQTranslation(models.Model):
    faq = models.ForeignKey(
        FAQ, on_delete=models.CASCADE, related_name="translations"
    )
    language = models.CharField(max_length=2)
    question = models.TextField()
    answer = RichTextField()

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["faq", "language"]
        verbose_name = "FAQ Translation"
        verbose_name_plural = "FAQ Translations"

    def __str__(self):
        return self.question[:50]


async def async_translate_faq(faq):
    async with Translator() as translator:
        tasks = []
        for lang, _ in settings.LANGUAGES:
            if lang == "en":
                continue

            tasks.append(
                asyncio.create_task(
                    translator.translate(faq.question, dest=lang)
                )
            )
            tasks.append(
                asyncio.create_task(
                    translator.translate(faq.answer, dest=lang)
                )
            )

        results = await asyncio.gather(*tasks)
        translations = list(
            zip(settings.LANGUAGES[1:], results[0::2], results[1::2])
        )
        for lang, translated_question, translated_answer in translations:
            await sync_to_async(FAQTranslation.objects.create)(
                faq=faq,
                language=lang[0],
                question=translated_question.text,
                answer=translated_answer.text,
            )


@receiver(post_save, sender=FAQ)
def create_faq_translations(sender, instance, created, **kwargs):
    if created:
        async_to_sync(async_translate_faq)(instance)
