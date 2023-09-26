from django.db import models

# Create your models here.


class BackendModel(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.title


class TesteModel(models.Model):
	id = models.IntegerField
	nome = models.TextField(max_length=255)
	score = models.TextField(max_length=255)
	senha = models.TextField(max_length=255)
	id_chefe = models.IntegerField()
	
	def __int__(self):
		return self.id
    
