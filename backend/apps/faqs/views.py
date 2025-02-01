from django.conf import settings
from django.core.cache import cache
from drf_spectacular.views import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FAQ, FAQTranslation
from .serializers import FAQSerializer, FAQTranslationSerializer


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="lang",
            description="Language code for translations (e.g., 'en', 'hi', 'bn')",
            required=False,
            type=str,
            default="en",
        ),
    ],
    responses={200: FAQSerializer(many=True)},
)
@api_view(["GET"])
def faq_list(request):
    """
    List all FAQs
    """

    lang = request.GET.get("lang", settings.LANGUAGE_CODE)
    cache_key = f"faqs_list:{lang}"

    # check if cached data exists
    cached_faqs = cache.get(cache_key)
    if cached_faqs:
        print("Cache hit")
        return Response(cached_faqs, status=status.HTTP_200_OK)

    # else fetch data from the database
    faqs = FAQ.objects.all()
    serializer = FAQSerializer(faqs, many=True, context={"request": request})

    # store in cache
    cache.set(cache_key, serializer.data, timeout=60 * 60 * 24)

    return Response(serializer.data, status=status.HTTP_200_OK)
