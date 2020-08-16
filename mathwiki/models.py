from django.db import models

# Create your models here.
class Axiom(models.Model):
    name = models.CharField(max_length = 300)
    summary = models.TextField(blank = True)
    statement = models.TextField()

    def __str__(self):
        return self.name

class MathematicalProperty(models.Model):
    name = models.CharField(max_length = 300)
    summary = models.TextField(blank = True)
    statement = models.TextField()
    applies_to = models.ManyToManyField('MathematicalObject')

    def __str__(self):
        return self.name


class MathematicalObject(models.Model):
    name = models.CharField(max_length = 300)
    summary = models.TextField(blank = True)
    definition = models.TextField()

    parent_objects = models.ForeignKey('self', on_delete = models.SET_NULL, null = True, blank = True)
    contains = models.ManyToManyField('self', blank = True, symmetrical = False, related_name = '+')

    properties = models.ManyToManyField(MathematicalProperty, blank = True)
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
    summary = models.TextField(blank = True)
    theorem_type = models.CharField(max_length = 1, choices = THEOREM_TYPE_CHOICES)
    proof = models.TextField()
    included_objects = models.ManyToManyField(MathematicalObject)
    def __str__(self):
        return self.name