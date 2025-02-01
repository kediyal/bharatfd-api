from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FAQ, FAQTranslation


@api_view(["GET"])
def faq_list(request):
    """
    List all FAQs
    """

    lang = request.GET.get("lang", settings.LANGUAGE_CODE)
    faqs = FAQ.objects.all()
    serialized_data = []

    for faq in faqs:
        translated_data = faq.get_translated(lang)
        serialized_data.append(
            {
                "id": faq.id,
                "question": translated_data["question"],
                "answer": translated_data["answer"],
                "created_at": faq.created_at,
                "updated_at": faq.updated_at,
            }
        )

    return Response(serialized_data, status=status.HTTP_200_OK)
