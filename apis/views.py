# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TesteSerializer
from .models import TesteModel


class TesteViewSet(viewsets.ModelViewSet):
	queryset = TesteModel.objects.all()

	serializer_class = TesteSerializer
