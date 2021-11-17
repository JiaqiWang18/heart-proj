from django.views.generic.list import ListView
from django.views.generic import DetailView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from disease.models import Disease
from disease.serializers import DiseaseSerializer
from rest_framework.permissions import AllowAny
import requests
import os


# Create your views here.
class DiseaseListView(ListView):
    template_name = 'disease/home.html'
    model = Disease
    context_object_name = 'disease_list'

    def __init__(self):
        super().__init__()
        self.search_value = ""

    def get_queryset(self):
        query = self.request.GET.get('search')

        if query:
            result = Disease.objects.filter(name__contains=query)
            self.search_value = query
        else:
            result = Disease.objects.all()
            self.search_value = ""
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.request.GET.get('tag')
        if tag:
            context['disease_list'] = self.get_queryset().filter(tags__slug=tag)
        context['search_value'] = self.search_value
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


@api_view(['GET'])
def tweets_list(request, disease):
    headers = {"Authorization": f"Bearer {os.environ.get('TWITTERTOKEN')}"}
    r = requests.get(f'https://api.twitter.com/1.1/search/tweets.json?q={disease}-filter:retweets AND -filter:replies&lang=en&count=10', headers=headers)
    return Response(r.json())
