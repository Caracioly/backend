from django.db import models


class TesteModel(models.Model):
	nome = models.TextField(max_length=255, help_text="Nome do usuário")
	score = models.TextField(max_length=255, help_text="Pontuação do usuário")
	senha = models.TextField(max_length=255, help_text="Senha do usuário")
	id_chefe = models.IntegerField(help_text="ID do chefe")
	
	def __str__(self):
		return self.nome
