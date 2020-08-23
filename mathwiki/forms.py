from django import forms
from .models import MathematicalObject, Theorem

class ObjectForm(forms.ModelForm):
    class Meta:
        model = MathematicalObject
        widgets = {
          'summary': forms.Textarea(attrs={'rows':2}),
          'definition': forms.Textarea(attrs={'rows':5}),
          'notes': forms.Textarea(attrs={'rows':4}),
          'parent_objects': forms.Select(attrs={'class':'ui dropdown'}),
          'properties': forms.SelectMultiple(attrs={'class':'ui dropdown'}),
          'contains': forms.SelectMultiple(attrs={'class':'ui dropdown'}),
        }
        fields = ['name', 'summary', 'definition', 'notes', 'parent_objects', 'contains', 'properties']

class TheoremForm(forms.ModelForm):
    class Meta:
        model = Theorem
        widgets = {
          'summary': forms.Textarea(attrs={'rows':2}),
          'proof': forms.Textarea(attrs={'rows':5}),
          'notes': forms.Textarea(attrs={'rows':4}),
          'included_objects': forms.SelectMultiple(attrs={'class':'ui dropdown'}),
        }
        fields = ['name', 'theorem_type', 'summary', 'hypothesis', 'conclusion', 'proof', 'notes', 'included_objects']