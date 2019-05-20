from django.shortcuts import render

from leavemanage.serializers import LeaveSerializer
from rest_framework import (authentication, generics, permissions, renderers,
                            status, viewsets)
from rest_framework.response import Response


class LeaveViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for posting a leave applicatons for employees
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

    def partial_update(self, request, pk=None):
        pass
