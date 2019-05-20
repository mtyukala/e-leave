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
            if data['start_date'] > data['end_date']:
                raise serializers.ValidationError(
                    _('The start date must come before the end date'))
        return data
