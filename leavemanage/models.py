from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext as _

STATUS = (('New', 'New'),
          ('Approved', 'Approved'),
          ('Declined', 'Declined'))
EMP_NUMBER_VALIDATOR = RegexValidator(r'[A-Z]{2}[0-9]{4}',
                                      _('Employee number format needs to be AA0000'))

TEL_NUMBER_VALIDATOR = RegexValidator(r'[0-9]{10}', _(
    'Phone number format needs to be #########'))
DATE_INPUT_FORMAT = ['%d-%m-%Y']


class Employee(models.Model):
    emp_number = models.CharField(blank=False, max_length=6,
                                  verbose_name=_("Employee Number"), validators=[EMP_NUMBER_VALIDATOR])
    phone_number = models.CharField(blank=False,
                                    max_length=10, verbose_name=_("Phone Number"), validators=[TEL_NUMBER_VALIDATOR])
    first_name = models.CharField(
        blank=False, max_length=25, verbose_name=_("First Name"))
    last_name = models.CharField(
        blank=False, max_length=30, verbose_name=_("Last Name"))

    class Meta:
        verbose_name = 'Employee'
        ordering = ['last_name', 'first_name', 'emp_number']
        unique_together = ['last_name', 'first_name', 'emp_number']

    def __str__(self):
        return self.fullname()

    def fullname(self):
        return '{0}. {1} {2} ({3})'.format(self.id, self.first_name, self.last_name, self.emp_number)


class Leave(models.Model):

    employee_pk = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now,
                                  verbose_name=_("Start Date"), blank=False)
    end_date = models.DateField(default=timezone.now,
                                verbose_name=_("End Date"), blank=False)
    days_of_leave = models.IntegerField(default=0)
    status = models.CharField(
        max_length=10, choices=STATUS, default=STATUS[0][0])

    class Meta:
        verbose_name = "Leave"
        ordering = ['start_date', 'end_date', 'employee_pk']
        unique_together = ['start_date', 'end_date', 'employee_pk']

    def __str__(self):
        return 'From {0} to {1} ({2} days)'.format(self.start_date, self.end_date, self.days_of_leave)
