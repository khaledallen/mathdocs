from django.contrib import admin

from .models import Definition, Theorem

# Register your models here.

admin.site.register(Definition)
admin.site.register(Theorem)