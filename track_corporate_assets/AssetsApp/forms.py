from django import forms
from django.utils import timezone
from .models import CheckOut

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = CheckOut
        fields = ('employee', 'device', 'condition')

class ReturnForm(forms.ModelForm):
    class Meta:
        model = CheckOut
        fields = ('checked_in', 'condition')

    def clean(self):
        cleaned_data = super().clean()
        checked_in = cleaned_data.get('checked_in')
        checkout = self.instance
        if checked_in and checked_in < checkout.checked_out:
            raise forms.ValidationError('Check-in date cannot be earlier than check-out date.')
        return cleaned_data
    

#serializers.py

"""
from rest_framework import serializers
from .models import Company, Employee, Device, CheckOut

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class CheckOutSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    device = DeviceSerializer()

    class Meta:
        model = CheckOut
        fields = '__all__'

"""