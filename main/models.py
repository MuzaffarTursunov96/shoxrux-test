from django.db import models

# Create your models here.



class Quetion(models.Model):
  choices=(
    ('a','a'),
    ('b','b'),
    ('c','c'),
    ('d','d'),
  )
  title =models.CharField(max_length=255)
  a =models.CharField(max_length=255)
  b=models.CharField(max_length=255)
  c=models.CharField(max_length=255)
  d=models.CharField(max_length=255)
  answer =models.CharField(max_length=20,choices=choices)

