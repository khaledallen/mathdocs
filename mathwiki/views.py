from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django import forms

from .models import MathematicalObject, Theorem
from .forms import ObjectForm, TheoremForm

# Create your views here.
def index(request):
    objects = MathematicalObject.objects.all()
    context = {'objects': objects}
    return render(request, 'mathwiki/index.html', context)

def object_details(request, object_id):
    object = get_object_or_404(MathematicalObject, pk=object_id)
    context = {'object': object}
    return render(request, 'mathwiki/mathobjectdetails.html', context)

class CreateObject(View):
    form_class = ObjectForm
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

class EditObject(View):
    form_class = ObjectForm
    template_name = 'mathwiki/edit_object.html'

    def get(self, request, object_id, **kwargs):
        object = MathematicalObject.objects.get(pk=object_id)
        form = self.form_class(instance=object)
        return render(request, self.template_name, {'form': form, 'object': object })

    def post(self, request, object_id, **kwargs):
        object = MathematicalObject.objects.get(pk=object_id)
        form = self.form_class(request.POST, instance=object)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect('/objects/{}'.format(object_id))
        return render(request, self.template_name, {'form': form})

def theorem_details(request, theorem_id):
    theorem = get_object_or_404(Theorem, pk=theorem_id)
    context = {'theorem': theorem, 'theorem_type_display': theorem.get_theorem_type_display() }
    return render(request, 'mathwiki/theoremdetails.html', context)
class CreateTheorem(View):
    form_class = TheoremForm
    template_name = 'mathwiki/create_theorem.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            new_thm = form.save()
            return HttpResponseRedirect('/theorems/{}'.format(new_thm.id))
        return render(request, self.template_name, {'form': form})

class EditTheorem(View):
    form_class = TheoremForm
    template_name = 'mathwiki/create_theorem.html'

    def get(self, request, theorem_id, **kwargs):
        theorem = Theorem.objects.get(pk=theorem_id)
        form = self.form_class(instance=object)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=theorem)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect('/objects/{}'.format(theorem_id))

        return render(request, self.template_name, {'form': form})