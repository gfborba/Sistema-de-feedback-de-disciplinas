from django.db import models

class Disciplinas(models.Model):
    nome = models.CharField(max_length=50)
    professor = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)

    def _str_(self):
        return self.nome

