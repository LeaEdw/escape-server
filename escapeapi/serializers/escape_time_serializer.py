from rest_framework import serializers
from escapeapi.models import EscapeTime

class EscapeTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscapeTime
        fields = ['id', 'user', 'game', 'approval_status', 'escape_time', 'submitted_at', 'admin_notes']