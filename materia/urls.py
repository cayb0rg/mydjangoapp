from django.urls import path

from . import views

app_name = "materia"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"), # pass in route and view and name
]