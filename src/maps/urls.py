from django.urls import path
from . import views

urlpatterns = [
    path("", views.maps_index, name="maps_index"),
    path("full/", views.maps_full, name="maps_full"),

]
