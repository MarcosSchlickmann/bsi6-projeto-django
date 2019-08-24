from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_list, name='dashboard_list'),
    path('dashboards/', views.dashboard_list, name='dashboard_list'),
    path('dashboards/new/', views.dashboard_new, name='dashboard_new'),
    path('dashboards/<int:pk>/', views.dashboard_detail, name='dashboard_detail'),
    path('dashboards/<int:pk>/edit/', views.dashboard_edit, name='dashboard_edit'),
    path('dashboards/<int:pk>/delete/', views.dashboard_delete, name='dashboard_delete')
]
