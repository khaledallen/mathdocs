from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('definitions/<int:definition_id>/', views.definitiondetails, name="definition details")
]