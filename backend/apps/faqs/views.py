from django.conf import settings
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
    faqs = FAQ.objects.all()

    serializer = FAQSerializer(faqs, many=True, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)
