from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.gallery, name="gallery"),
    path('photo/<str:pk>/',views.viewPhoto, name="viewPhoto"),
    path('add/',views.addPhoto, name="addPhoto"),
]
