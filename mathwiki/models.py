from django.db import models

# Create your models here.
class Axiom(models.Model):
    title = models.CharField(max_length = 300)
    statement = models.TextField()

class Definition(models.Model):
    name = models.CharField(max_length = 300)
    statement = models.TextField()
    def __str__(self):
        return self.name
    
class Theorem(models.Model):
    THEOREM_TYPE_CHOICES = (
        ('L', 'Lemma'),
        ('C', 'Corollary'),
        ('P', 'Proposition'),
        ('T', 'Theorem')
    )
    name = models.CharField(max_length = 300)
    theorem_type = models.CharField(max_length = 1, choices = THEOREM_TYPE_CHOICES)
    proof = models.TextField()
    included_definitions = models.ManyToManyField(Definition)
    def __str__(self):
        return self.name