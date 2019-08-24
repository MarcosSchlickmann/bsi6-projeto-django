from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views import View
from .models import Dashboard
from .forms import DashboardForm


# Create your views here.

def dashboard_list(request):
    dashboards = Dashboard.objects.all()
    return render(request, "app/dashboard_list.html", {'dashboards': dashboards})


def dashboard_detail(request, pk):
	dashboard = get_object_or_404(Dashboard, pk=pk)
	return render(request, 'app/dashboard_detail.html', {'dashboard': dashboard})


def dashboard_new(request):
	if request.method == 'POST':
		form = DashboardForm(request.POST)
		if form.is_valid():
			dashboard = form.save()
			return redirect('dashboard_detail', pk=dashboard.pk)
	else:
		form = DashboardForm()
	return render(request, 'app/dashboard_edit.html', {'form': form})


def dashboard_edit(request, pk):
	dashboard = get_object_or_404(Dashboard, pk=pk)
	if request.method == 'POST':
		form = DashboardForm(request.POST, instance=dashboard)
		if form.is_valid():
			dashboard = form.save()
			return redirect('dashboard_detail', pk=dashboard.pk)
	else:
		form = DashboardForm(instance=dashboard)
	return render(request, 'app/dashboard_edit.html', {'form': form})


def dashboard_delete(request, pk):
	dashboard = get_object_or_404(Dashboard, pk=pk)
	dashboard.delete()
	return redirect('dashboard_list')