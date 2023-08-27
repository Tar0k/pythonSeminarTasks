from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Index(TemplateView):
    template_name = "htmltasks/index.html"


class Catalog(TemplateView):
    template_name = "htmltasks/catalog.html"