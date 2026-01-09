# frases/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkViewSet, QuoteViewSet
from django.http import JsonResponse

router = DefaultRouter()
router.register('works', WorkViewSet, basename='work')
router.register('quotes', QuoteViewSet, basename='quote')

def health(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('', include(router.urls)),
    path('health/', health)
]