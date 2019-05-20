from django.urls import include, path

from leavemanage.models import Leave
from leavemanage.views import LeaveViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'^leave/', LeaveViewSet.as_view({
    'post': 'create',
    'put': 'put'
}), base_name='leave')

app_name = "leavemanage"

urlpatterns = [
    path('', include(router.urls))
]
