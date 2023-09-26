from django.shortcuts import render

# Create your views here.
# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import GeeksSerializer, TesteSerializer
from .models import BackendModel, TesteModel

# create a viewset


class GeeksViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = BackendModel.objects.all()

	# specify serializer to be used
	serializer_class = GeeksSerializer


class TesteViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = TesteModel.objects.all()

	# specify serializer to be used
	serializer_class = TesteSerializer
