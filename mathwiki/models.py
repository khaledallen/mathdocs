from django.db import models

# Create your models here.
class Definition(models.Model):
    title = models.CharField(max_length = 200)
    statement = models.TextField()
    
class Theorem(models.Model):
    title = models.CharField(max_length = 200)
    proof = models.TextField()
    included_definitions = models.ManyToManyField(Definition)