from django.urls import include, path

from .views import faq_list

urlpatterns = [
    path("", faq_list),
]
