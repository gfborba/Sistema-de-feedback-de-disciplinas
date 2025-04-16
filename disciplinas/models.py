from django.db import models
from django.contrib.auth.models import User

class Disciplinas(models.Model):
    nome = models.CharField(max_length=50)
    professor = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)

    def _str_(self):
        return self.nome

class Avaliacao(models.Model):
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.PositiveSmallIntegerField()
    comentario = models.CharField(max_length=500)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('disciplina', 'user')