from django.db import models

class Planta (models.Model):
    especie = models.CharField (max_length = 30)
    nome_cientifico = models.CharField (max_length= 30)
    ESTACAO = (
        ('P', 'Primavera'),
        ('V','Verão'),
        ('O','Outono'),
        ('I','Inverno'),
    ) 
    estacao= models.CharField (max_length=1, choices= ESTACAO, blank=False, null=False)
    
    def __str__ (self):
        return self.especie


class Vaso (models.Model):
    TAMANHO = (
        ('P', 'Pequeno'),
        ('M', 'Medio'),
        ('G', 'Grande'),
    ) 
    material = models.CharField (max_length = 30)
    tamanho = models.CharField (max_length=1, choices=TAMANHO, blank=False, null=False)

    def __str__ (self):
        return self.tamanho 

# Create your models here.
