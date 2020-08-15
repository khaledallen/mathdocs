from django.shortcuts import render
from django.http import HttpResponse

from .models import Definition

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the mathwiki index.")

def definitiondetails(request, definition_id):
    definition = Definition.objects.filter(id=definition_id)[0]
    context = {'definition': definition}
    return render(request, 'mathwiki/definitiondetails.html', context)