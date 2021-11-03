from django.shortcuts import render
from rest_framework import generics
from disease.models import Disease
from disease.serializers import DiseaseSerializer
from rest_framework.permissions import AllowAny


# Create your views here.
class DiseaseList(generics.ListAPIView):
    queryset = Disease.objects.all().order_by('name')
    serializer_class = DiseaseSerializer
    permission_classes = [AllowAny]
