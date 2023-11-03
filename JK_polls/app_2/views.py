from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
def index(request):
    param1 = ["momo","jojo"]
    context = {"param1": param1}
    return render(request, "app_2/index.html", context)