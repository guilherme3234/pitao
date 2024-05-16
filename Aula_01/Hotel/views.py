from django.db import models 

# Create your views here.

TIPO_QUARTOS = (
    ("SOLTEIRO", "solteiro"),
    ("CASAL","casal"),
    ("CONFORTO","conforto"),
    ("LUXO","luxo")
    )

class Hotel(models.model):
    titulo = models.charField(max_Leght=50)
    Descricao = models.TexFeld(max_leght=500 )

    def __str__(self):
        return self.titulo

class quarto(models.model):
    tipo = models.charField(max_leght= 15, choices = TIPO_QUARTOS)
    disponibilidade = models.IntergerFied()
    valor = models.FloatField (max_leght =4)
    descricao = models.TexFeld(max_leght=225)
    
    def __str__(self):
        return self.tipo
    


