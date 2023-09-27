# import serializer from rest_framework
from rest_framework import serializers
from .models import TesteModel


class TesteSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = TesteModel
		fields = ('id', 'nome', 'score', 'senha', 'id_chefe')