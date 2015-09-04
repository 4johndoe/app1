from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from estate.models import Filiya


def home(request):
    filies = Filiya.objects.all();
    return render(request, 'estate/home.html')


def about(request):
    return render_to_response('estate/about.html')