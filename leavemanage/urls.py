from django.urls import path

from leavemanage.views import LeaveViewSet
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path(r'docs/', include_docs_urls(title='Leave Management API Documentation')),
    path(r'leave/', LeaveViewSet.as_view({'post': 'create',
                                          'put': 'put'}), name='leave')
]
