from django.shortcuts import render
from rest_framework import viewsets
from . serializers import FoodsSerializer
from . models import Foods

class Foodsviewset(viewsets.ModelViewSet):
    queryset = Foods.objects.all().order_by('Mfd_id')
    serializer_class = FoodsSerializer

# Create your views here.
