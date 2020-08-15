from django.contrib import admin

from .models import Axiom, MathematicalProperty, MathematicalObject, Theorem

# Register your models here.

admin.site.register(Axiom)
admin.site.register(MathematicalProperty)
admin.site.register(MathematicalObject)
admin.site.register(Theorem)