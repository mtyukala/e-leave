from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext as _

# Create your models here.
STATUS = (('New', 'New'),
          ('Approved', 'Approved'),
          ('Declined', 'Declined'))


class Employee(models.Model):
    emp_number = models.CharField(
        max_length=10, verbose_name=_("Employee Number"))
    phone_number = models.CharField(
        max_length=10, verbose_name=_("Phone Number"))
    first_name = models.CharField(max_length=25, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=30, verbose_name=_("Last Name"))


class Leave(models.Model):

    employee_pk = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now,
                                      verbose_name=_("Start Date"), blank=False)
    end_date = models.DateTimeField(default=timezone.now,
                                    verbose_name=_("End Date"), blank=False)
    days_of_leave = models.IntegerField()
    status = models.CharField(
        max_length=10, choices=STATUS, default=STATUS[1][1])

    class Meta:
        verbose_name = "Leave"
        ordering = ['start_date', 'end_date', 'emp_number']
        unique_together = ['start_date', 'end_date', 'emp_number']
