from django.test import TestCase
from django.urls import reverse

from leavemanage.models import STATUS, Employee, Leave


# Create your tests here.


def create_leave(pk, start, end, days, status):
    return Leave.objects.create(employee_pk_id=pk, start_date=start,
                                end_date=end, days_of_leave=days, status=status)


def create_employee(number, phone, name, surname):
    return Employee.objects.create(emp_number=number, phone_number=phone,
                                   first_name=name, last_name=surname)


class LeaveViewTest(TestCase):
    def test_duplicate(self):
        """
        Leave application for one employee cannot be added twice
        """
        employee = create_employee('TC2000', '0987654321', 'Jean', 'Sean')
        leave = {'employee_pk': employee.id, 'start_date': '2020-01-02',
                 'end_date': '2020-01-07', 'days_of_leave': 6, 'status': STATUS[1][1]}
        response = self.client.post(
            path=reverse('leavemanage:leave'), data=leave)
        # self.assertEqual(Leave.objects.latest().start_date, '2020-01-02')
        self.assertEqual(response.status_code, 201)

    def test_create(self):
        """
        Leave application can be created
        """
        employee = create_employee('TS33', '2222222222', 'Billy', 'Bob')

        leave = {'employee_pk': employee.id, 'start_date': '2020-01-02',
                 'end_date': '2020-01-07', 'days_of_leave': 6, 'status': STATUS[1][1]}

        response = self.client.post(
            path=reverse('leavemanage:leave'), data=leave)
        # print(response)
        self.assertEqual(response.status_code, 201)

    def test_start_date_in_past(self):
        """
        The start date of a leave application cannot be in the past
        """
        employee = create_employee('TS8877', '1234567890', 'Johan', 'Sinque')
        leave = {'employee_pk': employee.id, 'start_date': '2016-01-02',
                 'end_date': '2020-01-01', 'days_of_leave': 6, 'status': STATUS[1][1]}

        response = self.client.post(
            path=reverse('leavemanage:leave'), data=leave)
        self.assertEqual(response.status_code, 400)

    def test_end_date_before(self):
        """
        The end date of a leave application cannot be before the start date
        """
        employee = create_employee('TS0077', '1234563390', 'Jorah', 'Mommon')

        leave = {'employee_pk': employee.id, 'start_date': '2019-06-02',
                 'end_date': '2019-01-01', 'days_of_leave': 6, 'status': STATUS[1][1]}

        response = self.client.post(
            path=reverse('leavemanage:leave'), data=leave)
        self.assertEqual(response.status_code, 400)
