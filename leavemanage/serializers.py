

from django.utils import timezone
from django.utils.translation import ugettext as _

from leavemanage.models import Leave
from rest_framework import serializers


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        depth = 1
        fields = ('__all__')

    def validate(self, data):
        if 'start_date' in data and 'end_date' in data:
            today = timezone.now
            start = data['start_date']
            end = data['end_date']

            if start < today or start > end:
                raise serializers.ValidationError(
                    _('The start date must come before the end date'))
        return data
