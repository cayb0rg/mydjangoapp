from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.
from .models import Widget

from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = "materia/index.html"
    context_object_name = "widget_list"

    def get_queryset(self):
        """Return all widgets."""
        return Widget.objects.all()

def index(request):
    widget_list = Widget.objects.all()
    template = loader.get_template("materia/index.html")
    context = {
        "widget_list": widget_list,
    }
    return HttpResponse(template.render(context, request))
