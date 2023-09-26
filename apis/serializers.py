# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import BackendModel, TesteModel


# Create a model serializer
class GeeksSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = BackendModel
		fields = ('title', 'description')


class TesteSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = TesteModel
		fields = ('id', 'nome', 'score', 'senha', 'id_chefe')