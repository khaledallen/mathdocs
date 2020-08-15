from django.shortcuts import render
from django.http import HttpResponse

from .models import MathematicalObject

# Create your views here.
def index(request):
    objects = MathematicalObject.objects.all()
    context = {'objects': objects}
    return render(request, 'mathwiki/index.html', context)

def object_details(request, object_id):
    object = MathematicalObject.objects.filter(id=object_id)[0]
    context = {'object': object}
    return render(request, 'mathwiki/mathobjectdetails.html', context)