# frases/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkViewSet, QuoteViewSet

router = DefaultRouter()
router.register('works', WorkViewSet, basename='work')
router.register('quotes', QuoteViewSet, basename='quote')

urlpatterns = [
    path('', include(router.urls)),
]