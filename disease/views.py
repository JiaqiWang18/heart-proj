from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from rest_framework import generics
from disease.models import Disease
from disease.serializers import DiseaseSerializer
from rest_framework.permissions import AllowAny


# Create your views here.
class DiseaseListView(ListView):
    template_name = 'disease/home.html'
    model = Disease
    context_object_name = 'disease_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DiseaseDetailView(DetailView):
    template_name = 'disease/disease_detail.html'
    model = Disease
    context_object_name = 'disease'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DiseaseList(generics.ListAPIView):
    queryset = Disease.objects.all().order_by('name')
    serializer_class = DiseaseSerializer
    permission_classes = [AllowAny]
