from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone
from .models import Company, Employee, Device, CheckOut
from .forms import CheckOutForm, ReturnForm

def index(request):
    companies = Company.objects.all()
    return render(request, 'asset_tracker/ABC.html', {'companies': companies})

def device_list(request):
    devices = Device.objects.all()
    return render(request, 'asset_tracker/ABC.html', {'devices': devices})

def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    checkouts = CheckOut.objects.filter(device=device).order_by('-checked_out')
    return render(request, 'asset_tracker/ABC.html', {'device': device, 'checkouts': checkouts})

def device_add(request):
    if request.method == 'POST':
        form = CheckOutForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.checked_out = timezone.now()
            device.save()
            messages.success(request, f'{device.device} was successfully checked out to {device.employee}.')
            return redirect(reverse('asset_tracker:device_detail', args=[device.device.pk]))
    else:
        form = CheckOutForm()
    return render(request, 'asset_tracker/ABC.html', {'form': form, 'title': 'Check Out Device'})

def device_edit(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == 'POST':
        form = ReturnForm(request.POST, instance=device.checkout_set.filter(checked_in__isnull=True).first())
        if form.is_valid():
            checkout = form.save(commit=False)
            checkout.checked_in = timezone.now()
            checkout.save()
            messages.success(request, f'{device} was successfully checked in.')
            return redirect(reverse('asset_tracker:device_detail', args=[device.pk]))
    else:
        form = ReturnForm(instance=device.checkout_set.filter(checked_in__isnull=True).first())
    return render(request, 'asset_tracker/ABC.html', {'form': form, 'title': 'Check In Device'})

def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    employees = Employee.objects.filter(company=company)
    devices = Device.objects.filter(company=company)
    checkouts = CheckOut.objects.filter(device__in=devices).order_by('-checked_out')
    return render(request, 'asset_tracker/ABC.html', {'company': company, 'employees': employees, 'devices': devices, 'checkouts': checkouts})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    devices = Device.objects.filter(company=employee.company)
    checkouts = CheckOut.objects.filter(employee=employee).order_by('-checked_out')
    return render(request, 'asset_tracker/ABC.html', {'employee': employee, 'devices': devices, 'checkouts': checkouts})
