from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django import forms

from .models import MathematicalObject

# Create your views here.
def index(request):
    objects = MathematicalObject.objects.all()
    context = {'objects': objects}
    return render(request, 'mathwiki/index.html', context)

def object_details(request, object_id):
    object = get_object_or_404(MathematicalObject, pk=object_id)
    context = {'object': object}
    return render(request, 'mathwiki/mathobjectdetails.html', context)



class CreateObjectForm(forms.ModelForm):
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

class CreateObject(View):
    form_class = CreateObjectForm
    template_name = 'mathwiki/create_object.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            new_obj = form.save()
            print(new_obj.id)
            return HttpResponseRedirect('/objects/{}'.format(new_obj.id))

        return render(request, self.template_name, {'form': form})