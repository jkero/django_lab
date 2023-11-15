from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect

from .models import LeParam1

# Create your views here.
@csrf_protect
def index(request):
    param_nom = request
#    param_nom = "foque"
    context = {"param1": param_nom}
    return render(request, "app_2/index.html", context)
@csrf_protect
def create(request):
    param_nom = request
#    param_nom = "foque"
    context = {"param1": param_nom}
    return render(request, "app_2/index.html", context)

@csrf_protect
def create_note(request):
    param = LeParam1()
    param.param_nom = request.POST['nom']
    param.param_date = request.POST['date']
    param.save()

