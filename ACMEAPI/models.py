from django.db import models

class Tarefa(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(255)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    finalizada = models.BooleanField()