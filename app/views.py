from django.shortcuts import render, HttpResponse
from .models import Dashboard

# Create your views here.

def dashboard_list(request):
    dashboards = Dashboard.objects.all()
    return render(request, "app/dashboard_list.html", {'dashboards': dashboards})