from django.db import models

class Jogos(models.Model):
  title = models.CharField(max_length=30)
  genre = models.CharField(max_length=30)
  price = models.CharField(max_length=30)
  date = models.CharField(max_length=30)

class ThingsILike(models.Model):
  OPTIONS =[
    ("N","Not Often"),
    ("S","Some Times"),
    ("A","Always"),
  ]
  title = models.CharField(max_length=30)
  when = models.CharField(max_length=30)
  what = models.CharField(max_length=30)
  how_often = models.CharField(max_length=1, choices=OPTIONS)

# Create your models here.

# nome = models.CharField(max_length = 50)
# ano = models.DateField()
# n_musicas = models.IntegerField()
# real = models.BooleanField()
