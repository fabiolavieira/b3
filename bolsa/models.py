from django.db import models


class Pregao(models.Model):
    nome = models.CharField(max_length=40)
    codigo = models.CharField(max_length=5, unique=True)
    descricao = models.TextField()
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return self.nome


class Ativos(models.Model):
    acao = models.ForeignKey('Pregao', on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return self.acao.nome

