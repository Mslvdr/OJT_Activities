from django.urls import path
from . import views
urlpatterns = [
    path("index/", views.Index, name="index"),
    path("single-input/", views.SingleInput, name="single-input"),
    path("multiple-input/", views.MultipleInput, name="multiple-input"),
    path("output-single/", views.OutputDataSingle, name="output-single"),
    path("output-multiple/", views.OutputDataMultiple, name="output-multiple"),
]
