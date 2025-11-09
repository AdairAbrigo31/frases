from django.shortcuts import render
from rest_framework import viewsets
from .models import Work, Quote
from .serializers import WorkSerializer, QuoteSerializer

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
