from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse
from django import forms

from .models import MathematicalObject, Theorem, Axiom, MathematicalProperty
from .forms import ObjectForm, TheoremForm, AxiomForm, PropertyForm

# Create your views here.
def index(request):
    objects = MathematicalObject.objects.order_by('name').all()[:10]
    print(objects)
    context = {'objects': objects}
    return render(request, 'mathwiki/index.html', context)

def object_details(request, object_id):
    object = get_object_or_404(MathematicalObject, pk=object_id)
    context = {'object': object}
    return render(request, 'mathwiki/mathobjectdetails.html', context)

class CreateObject(LoginRequiredMixin, View):
    form_class = ObjectForm
    form_template = 'mathwiki/shared/object_form.html'
    template_name = 'mathwiki/create_edit_form_wrapper.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form,
            'title': 'Create New Object',
            'form_action_url': reverse('create_object'),
            'form_template': self.form_template
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            new_obj = form.save()
            print(new_obj.id)
            return HttpResponseRedirect('/objects/{}'.format(new_obj.id))

        return render(request, self.template_name, {'form': form})

class EditObject(LoginRequiredMixin, View):
    form_class = ObjectForm
    form_template = 'mathwiki/shared/object_form.html'
    template_name = 'mathwiki/create_edit_form_wrapper.html'

    def get(self, request, object_id, **kwargs):
        object = MathematicalObject.objects.get(pk=object_id)
        form = self.form_class(instance=object)
        context = {
            'object': object,
            'form': form,
            'title': 'Edit ' + object.name,
            'form_action_url': reverse('edit_object', args=[object.id]),
            'form_template': self.form_template
        }
        return render(request, self.template_name, context)

    def post(self, request, object_id, **kwargs):
        object = MathematicalObject.objects.get(pk=object_id)
        form = self.form_class(request.POST, instance=object)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect('/objects/{}'.format(object_id))

        context = {
            'object': object,
            'form': form,
            'title': 'Edit ' + object.name,
            'form_action': 'edit_object',
            'form_template': self.form_template
        }
        return render(request, self.template_name, context)

def theorem_details(request, theorem_id):
    theorem = get_object_or_404(Theorem, pk=theorem_id)
    context = {'theorem': theorem, 'theorem_type_display': theorem.get_theorem_type_display() }
    return render(request, 'mathwiki/theoremdetails.html', context)

class CreateTheorem(LoginRequiredMixin, View):
    form_class = TheoremForm
    form_template = 'mathwiki/shared/theorem_form.html'
    template_name = 'mathwiki/create_edit_form_wrapper.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form,
            'title': 'Create New Theorem',
            'form_action_url': reverse('create_theorem'),
            'form_template': self.form_template
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            new_thm = form.save()
            return HttpResponseRedirect('/theorems/{}'.format(new_thm.id))

        context = {
            'theorem': theorem,
            'form': form,
            'title': 'Edit ' + theorem.name,
            'form_action': 'edit_theorem',
            'form_template': self.form_template
        }
        return render(request, self.template_name, context)

class EditTheorem(LoginRequiredMixin, View):
    form_class = TheoremForm
    form_template = 'mathwiki/shared/theorem_form.html'
    template_name = 'mathwiki/create_edit_form_wrapper.html'

    def get(self, request, theorem_id, **kwargs):
        theorem = Theorem.objects.get(pk=theorem_id)
        form = self.form_class(instance=theorem)
        context = {
            'theorem': theorem,
            'form': form,
            'title': 'Edit ' + theorem.name,
            'form_action': 'edit_theorem',
            'form_template': self.form_template
        }
        return render(request, self.template_name, context)

    def post(self, request, theorem_id, **kwargs):
        theorem = Theorem.objects.get(pk=theorem_id)
        form = self.form_class(request.POST, instance=theorem)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect('/theorems/{}'.format(theorem_id))

        context = {
            'theorem': theorem,
            'form': form,
            'title': 'Edit ' + theorem.name,
            'form_action': 'edit_theorem',
            'form_template': self.form_template
        }
        return render(request, self.template_name, context)


def axiom_details(request, axiom_id):
    axiom = get_object_or_404(Axiom, pk=axiom_id)
    context = {'axiom': axiom}
    return render(request, 'mathwiki/axiomdetails.html', context)

class CreateAxiom(LoginRequiredMixin, View):
    form_class = AxiomForm
    form_template = 'mathwiki/shared/axiom_form.html'
    template_name = 'mathwiki/create_edit_form_wrapper.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form,
            'title': 'Create New Axiom',
            'form_action_url': reverse('create_axiom'),
            'form_template': self.form_template
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            new_axiom = form.save()
            return HttpResponseRedirect('/axioms/{}'.format(new_axiom.id))

        context = {
            'axiom': axiom,
            'form': form,
            'title': 'Edit ' + axiom.name,
            'form_action': 'edit_axiom',
            'form_template': self.form_template
        }
        return render(request, self.template_name, context)

class EditAxiom(LoginRequiredMixin, View):
    form_class = AxiomForm
    form_template = 'mathwiki/shared/axiom_form.html'
    template_name = 'mathwiki/create_edit_form_wrapper.html'

    def get(self, request, axiom_id, **kwargs):
        axiom = Axiom.objects.get(pk=axiom_id)
        form = self.form_class(instance=axiom)
        context = {
            'axiom': axiom,
            'form': form,
            'title': 'Edit ' + axiom.name,
            'form_action': 'edit_axiom',
            'form_template': self.form_template
        }
        return render(request, self.template_name, context)

    def post(self, request, axiom_id, **kwargs):
        axiom = Axiom.objects.get(pk=axiom_id)
        form = self.form_class(request.POST, instance=axiom)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect('/axioms/{}'.format(axiom_id))

        context = {
            'axiom': axiom,
            'form': form,
            'title': 'Edit ' + axiom.name,
            'form_action': 'edit_axiom',
            'form_template': self.form_template
        }
        return render(request, self.template_name, context)

def property_details(request, property_id):
    property = get_object_or_404(MathematicalProperty, pk=property_id)
    context = {'property': property}
    return render(request, 'mathwiki/propertydetails.html', context)

class CreateProperty(LoginRequiredMixin, View):
    form_class = PropertyForm
    form_template = 'mathwiki/shared/property_form.html'
    template_name = 'mathwiki/create_edit_form_wrapper.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form,
            'title': 'Create New Property',
            'form_action_url': reverse('create_property'),
            'form_template': self.form_template
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            new_prop = form.save()
            return HttpResponseRedirect('/properties/{}'.format(new_prop.id))

        return render(request, self.template_name, {'form': form})

        # context = {
        #     'property': property,
        #     'form': form,
        #     'title': 'Edit ' + property.name,
        #     'form_action': 'edit_property',
        #     'form_template': self.form_template
        # }
        # return render(request, self.template_name, context)

class EditProperty(LoginRequiredMixin, View):
    form_class = PropertyForm
    form_template = 'mathwiki/shared/property_form.html'
    template_name = 'mathwiki/create_edit_form_wrapper.html'

    def get(self, request, property_id, **kwargs):
        property = MathematicalProperty.objects.get(pk=property_id)
        form = self.form_class(instance=property)
        context = {
            'property': property,
            'form': form,
            'title': 'Edit ' + property.name,
            'form_action': 'edit_property',
            'form_template': self.form_template
        }
        return render(request, self.template_name, context)

    def post(self, request, property_id, **kwargs):
        property = MathematicalProperty.objects.get(pk=property_id)
        form = self.form_class(request.POST, instance=property)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect('/properties/{}'.format(property_id))

        context = {
            'property': property,
            'form': form,
            'title': 'Edit ' + property.name,
            'form_action': 'edit_property',
            'form_template': self.form_template
        }
        return render(request, self.template_name, context)