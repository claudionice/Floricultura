from django.db import models

class plantas (models.Model):
    especie = models.CharField (max_length = 30)
    nome_cientifico = models.CharField (max_length= 30)
    ESTACAO = (
        ('Primavera'),
        ('Verão'),
        ('Outono'),
        ('Inverno'),
    ) 
    estacao= models.CharField (max_length=1, choices= ESTACAO, blank=False, null=False)
    
    def __str__ (self):
        return self.especie


class vaso (models.Model):
    material = models.CharField (max_length = 30)
    TAMANHO = (
        ('P', 'Pequeno'),
        ('M', 'Medio'),
        ('G', 'Grande'),
    ) 
    tamanho = models.CharField (max_length=1, choices=TAMANHO, blank=False, null=False)

    def __str__ (self):
        return self.tamanho 

# Create your models here.
