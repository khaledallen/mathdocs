from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('objects/<int:object_id>/', views.object_details, name="object_details"),
    path('objects/create/', views.CreateObject.as_view(), name="create_object"),
    path('objects/edit/<int:object_id>', views.EditObject.as_view(), name="edit_object"),

    path('theorems/<int:theorem_id>/', views.theorem_details, name="theorem_details"),
    path('theorems/create/', views.CreateTheorem.as_view(), name="create_theorem"),
    path('theorems/edit/<int:theorem_id>', views.EditTheorem.as_view(), name="edit_theorem"),

]