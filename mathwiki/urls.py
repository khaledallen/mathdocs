from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('objects/<int:object_id>/', views.object_details, name="object_details"),
    path('objects/create/', views.CreateObject.as_view(), name="create_object"),
]