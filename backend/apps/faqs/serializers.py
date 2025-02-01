from rest_framework import serializers

from .models import FAQ, FAQTranslation


class FAQTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQTranslation
        fields = ["language", "question", "answer"]


class FAQSerializer(serializers.ModelSerializer):
    translations = FAQTranslationSerializer(many=True, read_only=True)

    class Meta:
        model = FAQ
        fields = [
            "id",
            "question",
            "answer",
            "created_at",
            "updated_at",
            "translations",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
