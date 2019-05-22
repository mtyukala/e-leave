from django.urls import path

from leavemanage.views import LeaveViewSet

app_name = 'leavemanage'
urlpatterns = [
    path(r'leave/', LeaveViewSet.as_view({'post': 'create',
                                          'put': 'put'}), name='leave')
]
