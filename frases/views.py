from django.shortcuts import render
from rest_framework import viewsets
from .models import Work, Quote
from .serializers import WorkSerializer, QuoteSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    def get_permissions(self):
        # POST y GET son públicos
        if self.action in ['create', 'list', 'retrieve']:
            return [AllowAny()]
        # PUT, PATCH, DELETE requieren autenticación
        return [IsAuthenticated()]

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]
