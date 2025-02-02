import pytest
from apps.faqs.models import FAQ, FAQTranslation
from django.conf import settings
from django.core.cache import cache


@pytest.mark.django_db
class TestFAQModel:
    def setup_method(self):
        cache.clear()

    def test_faq_creation(self):
        """Test that an FAQ object is created successfully."""
        faq = FAQ.objects.create(
            question="What is Django?", answer="A web framework."
        )

        assert faq.id is not None
        assert faq.question == "What is Django?"
        assert faq.answer == "A web framework."

    def test_str_method(self):
        """Test the string representation of FAQ"""
        long_question = "x" * 60
        faq = FAQ.objects.create(question=long_question, answer="test")
        assert str(faq) == long_question[:50]

    def test_ordering(self):
        """Test FAQs are ordered by created_at in descending order"""
        faq1 = FAQ.objects.create(question="First", answer="1")
        faq2 = FAQ.objects.create(question="Second", answer="2")
        faqs = FAQ.objects.all()
        assert faqs[0] == faq2
        assert faqs[1] == faq1

    def test_faq_creates_translations(self):
        """Ensure creating an FAQ triggers auto-translation into supported languages."""
        faq = FAQ.objects.create(
            question="What is FD?", answer="A fixed deposit."
        )

        # Ensure translations are created for all supported languages
        assert (
            FAQTranslation.objects.filter(faq=faq).count()
            == len(settings.LANGUAGES) - 1
        )

    def test_get_translated_cache_hit(self):
        """Test getting translated content from cache"""
        faq = FAQ.objects.create(question="Cache test?", answer="Test.")
        cached_data = {"question": "Cached Q", "answer": "Cached A"}
        lang = "hi"
        cache_key = f"faq_translation:{faq.id}:{lang}"
        cache.set(cache_key, cached_data)

        result = faq.get_translated(lang=lang)
        assert result == cached_data

    def test_get_translated_existing_translation(self):
        """Test getting translated content from database"""
        faq = FAQ.objects.create(question="Original", answer="Answer")

        result = faq.get_translated(lang="hi")
        assert result["question"] == "मूल"
        assert result["answer"] == "उत्तर"


@pytest.mark.django_db
class TestFAQTranslationModel:
    def test_str_method(self):
        """Test the string representation of FAQTranslation"""
        faq = FAQ.objects.create(question="Original", answer="Answer")
        translation = faq.translations.get(language="hi")
        assert str(translation) == translation.question[:50]

    def test_unique_together_constraint(self):
        "Test that FAQTranslation enforces unique_together constraint"
        faq = FAQ.objects.create(question="Original", answer="Answer")

        with pytest.raises(Exception):
            FAQTranslation.objects.create(
                faq=faq,
                language="hi",
                question="Original 2",
                answer="Answer 2",
            )


@pytest.mark.django_db
class TestCaching:
    def setup_method(self):
        cache.clear()

    def test_cache_cleared_on_faq_save(self):
        """Test that cache is cleared when an FAQ is saved."""
        faq = FAQ.objects.create(question="Original", answer="Answer")

        cache.set("test_key", "test_value")

        faq.question = "What is Django? Updated"
        faq.save()

        assert cache.get("test_key") is None

    def test_cache_cleared_on_translation_save(self):
        """Test that cache is cleared when translation is saved"""
        faq = FAQ.objects.create(question="Original", answer="Answer")

        translation = faq.translations.get(language="hi")
        cache.set("test_key", "test_value")
        translation.question = "Updated Spanish"
        translation.save()

        assert cache.get("test_key") is None

    def test_cache_cleared_on_delete(self):
        """Test that cache is cleared when FAQ or translation is deleted"""
        faq = FAQ.objects.create(question="Original", answer="Answer")
        cache.set("test_key", "test_value")

        faq.delete()
        assert cache.get("test_key") is None
