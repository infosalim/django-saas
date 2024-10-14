from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    queryset = PageVisit.objects.filter(path=request.path)
    my_title = "Django SaaS App"
    my_context = {"page_title": my_title, "page_visit_count": queryset.count()}
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)
