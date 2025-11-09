# frases/serializers.py
from rest_framework import serializers
from .models import Work, Quote

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    quotes = QuoteSerializer(many=True, read_only=True)
    
    class Meta:
        model = Work
        fields = '__all__'