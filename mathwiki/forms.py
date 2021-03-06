from django import forms
from .models import MathematicalObject, Theorem, Axiom, MathematicalProperty

class LatexPreviewTextarea(forms.widgets.Textarea):
    template_name = 'mathwiki/forms/widgets/latexpreviewtextarea.html'
    input_type = 'text'

    def get_context(self, name, value, attrs):
          context = super(LatexPreviewTextarea, self).get_context(name, value, attrs)
          return context


class ObjectForm(forms.ModelForm):
    class Meta:
        model = MathematicalObject
        widgets = {
          'summary': LatexPreviewTextarea(attrs={'rows':2}),
          'definition': LatexPreviewTextarea(attrs={'rows':5}),
          'notes': LatexPreviewTextarea(attrs={'rows':4}),
          'examples': LatexPreviewTextarea(attrs={'rows':4}),
          'parent_objects': forms.Select(attrs={'class':'ui dropdown'}),
          'properties': forms.SelectMultiple(attrs={'class':'ui dropdown'}),
          'contains': forms.SelectMultiple(attrs={'class':'ui dropdown'}),
          'used_in': forms.SelectMultiple(attrs={'class':'ui dropdown'})
        }
        fields = ['name', 'summary', 'definition', 'examples', 'notes', 'parent_objects', 'contains', 'properties', 'used_in']

class TheoremForm(forms.ModelForm):
    class Meta:
        model = Theorem
        widgets = {
          'summary': LatexPreviewTextarea(attrs={'rows':2}),
          'proof': LatexPreviewTextarea(attrs={'rows':5}),
          'hypothesis': LatexPreviewTextarea(attrs={'rows':5}),
          'conclusion': LatexPreviewTextarea(attrs={'rows':5}),
          'examples': LatexPreviewTextarea(attrs={'rows':5}),
          'notes': LatexPreviewTextarea(attrs={'rows':4}),
          'included_objects': forms.SelectMultiple(attrs={'class':'ui dropdown'}),
        }
        fields = ['name', 'theorem_type', 'summary', 'hypothesis', 'conclusion', 'proof', 'examples', 'notes', 'included_objects']

class AxiomForm(forms.ModelForm):
    class Meta:
        model = Axiom
        widgets = {
          'summary': LatexPreviewTextarea(attrs={'rows':2}),
          'statement': LatexPreviewTextarea(attrs={'rows':5}),
          'examples': LatexPreviewTextarea(attrs={'rows':5}),
          'notes': LatexPreviewTextarea(attrs={'rows':4}),
          'used_in': forms.SelectMultiple(attrs={'class':'ui dropdown'}),
        }
        fields = ['name', 'summary', 'statement', 'examples', 'notes', 'used_in']

class PropertyForm(forms.ModelForm):
    class Meta:
        model = MathematicalProperty
        widgets = {
          'summary': LatexPreviewTextarea(attrs={'rows':2}),
          'statement': LatexPreviewTextarea(attrs={'rows':5}),
          'examples': LatexPreviewTextarea(attrs={'rows':5}),
          'notes': LatexPreviewTextarea(attrs={'rows':4}),
          'applies_to': forms.SelectMultiple(attrs={'class':'ui dropdown'}),
        }
        fields = ['name', 'summary', 'statement', 'examples', 'notes', 'applies_to']