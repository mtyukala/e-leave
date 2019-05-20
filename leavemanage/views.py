from django.shortcuts import render

from leavemanage.serializers import LeaveSerializer
from rest_framework import (authentication, generics, permissions, renderers,
                            status, viewsets)
from rest_framework.response import Response


class LeaveViewSet(viewsets.ModelViewSet):
    """
    Leave create Api end point, clients need to submit `employee_pk`,
    `start_date`, `end_date`, `days_of_leave`
    and `status` (optional, defaults to New)
    """
    serializer_class = LeaveSerializer

    def create(self, request, *args, **kwargs):
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            headers = self.get_success_headers(serializer.data)
            serializer = LeaveSerializer(instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        """
        Leave update API end point.
        """
        return self.update(request, *args, **kwargs)
