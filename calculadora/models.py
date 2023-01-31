from django.db import models

class Categoria(models.Model):
    options = (
        ("café da manhã", "café da manhã"),
        ("almoço", "almoço"),
        ("café da tarde", "café da tarde"),
        ("janta", "janta"),
        ("ceia", "ceia"),
    )

    nome = models.CharField(max_length=65, choices=options)

    def __str__(self):
        return str(self.nome)

class Alimento(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.ManyToManyField(Categoria)
    carboidratos = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    proteinas = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    gorduras_totais = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    calorias = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    quantidade = models.IntegerField(default=1, null=True, blank=True)
    
    def __str__(self):
        return str(self.nome)
