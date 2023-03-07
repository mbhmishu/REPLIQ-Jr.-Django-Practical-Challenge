from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CheckOut(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checked_out = models.DateTimeField(default=timezone.now)
    checked_in = models.DateTimeField(blank=True, null=True)
    condition = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.employee} - {self.device}'

    def is_checked_in(self):
        return self.checked_in is not None

    def days_out(self):
        if self.is_checked_in():
            return (self.checked_in - self.checked_out).days
        else:
            return (timezone.now() - self.checked_out).days