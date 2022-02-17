from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length = 50)
    editora = models.CharField(max_length = 20, blank = True)
    sinopse = models.TextField(blank = True)
    ano = models.IntegerField(blank = True)

    def __str__(self) -> str:
        return self.nome