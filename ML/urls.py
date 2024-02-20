from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("classification", views.classification, name="class"),
    path("regression", views.regression, name="reg"),
    path("predict/<int:pk>", views.predict, name="predict"),
]
