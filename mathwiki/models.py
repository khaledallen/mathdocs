from django.db import models

# Create your models here.
class Axiom(models.Model):
    name = models.CharField(max_length = 300)
    summary = models.TextField(blank = True)
    statement = models.TextField()
    notes = models.TextField(blank = True)
    examples = models.TextField(blank = True)
    used_in = models.ManyToManyField('Theorem', blank = True, symmetrical = False)

    def __str__(self):
        return self.name

class MathematicalProperty(models.Model):
    name = models.CharField(max_length = 300)
    summary = models.TextField(blank = True)
    statement = models.TextField()
    notes = models.TextField(blank = True)
    examples = models.TextField(blank = True)
    applies_to = models.ManyToManyField('MathematicalObject', blank = True, symmetrical = False)

    def __str__(self):
        return self.name

class MathematicalObject(models.Model):
    name = models.CharField(max_length = 300)
    summary = models.TextField(blank = True)
    definition = models.TextField()
    examples = models.TextField(blank = True)
    notes = models.TextField(blank = True)
    used_in = models.ManyToManyField('Theorem', blank = True, symmetrical = False)

    parent_objects = models.ForeignKey('self', on_delete = models.SET_NULL, null = True, blank = True)
    contains = models.ManyToManyField('self', blank = True, symmetrical = False, related_name = '+')

    properties = models.ManyToManyField(MathematicalProperty, blank = True, symmetrical = False)
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
    notes = models.TextField(blank = True)
    hypothesis = models.TextField(blank = True)
    conclusion = models.TextField(blank = True)
    theorem_type = models.CharField(max_length = 1, choices = THEOREM_TYPE_CHOICES)
    proof = models.TextField()
    examples = models.TextField(blank = True)
    references = models.ManyToManyField('self', blank=True, symmetrical=False)
    included_objects = models.ManyToManyField(MathematicalObject, blank = True, symmetrical=False)
    def __str__(self):
        return self.name