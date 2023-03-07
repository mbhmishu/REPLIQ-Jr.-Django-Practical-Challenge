from django.urls import path
from . import views

app_name = 'asset_tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('devices/', views.device_list, name='device_list'),
    path('devices/<int:pk>/', views.device_detail, name='device_detail'),
    path('devices/add/', views.device_add, name='device_add'),
    path('devices/<int:pk>/edit/', views.device_edit, name='device_edit'),
    path('companies/<int:pk>/', views.company_detail, name='company_detail'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
]
