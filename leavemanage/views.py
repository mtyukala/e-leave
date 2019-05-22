from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.utils.translation import ugettext as _

from leavemanage.models import Employee, Leave
from leavemanage.serializers import LeaveSerializer
from rest_framework import (authentication, generics, permissions, renderers,
                            status, viewsets)
from rest_framework.response import Response


class LeaveViewSet(viewsets.ModelViewSet):
    """
    create:
    Leave create Api end point, clients need to submit `employee_pk`,
    `start_date`, `end_date`, `days_of_leave`
    and `status` (optional, defaults to New). Acceptable date format is: YYY-MM-DD
    Assumpation: One or many leave applications are passed to /leave/
    """
    serializer_class = LeaveSerializer
    querset = Leave.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = LeaveSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)  # Trigger HTTP_400
        id = request.data['employee_pk']
        start = request.data['start_date']
        end = request.data['end_date']
        stop = id is None or start is None or end is None
        if stop or Leave.objects.filter(employee_pk__id=id, start_date=start, end_date=end).exists():
            # errors = serializer.errors
            return Response({
                'status': _('Bad request'),
                'message': _('Duplicate leave application'),
            }, status=status.HTTP_400_BAD_REQUEST)

        instance = serializer.save(
            employee_pk_id=id)
        headers = self.get_success_headers(serializer.data)
        serializer = LeaveSerializer(instance)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def put(self, request, *args, **kwargs):
        """
        Leave update API end point.
        """
        return self.update(request, *args, **kwargs)
