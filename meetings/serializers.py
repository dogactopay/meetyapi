from rest_framework import serializers
from .models import Meetings
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from tangible.serializers import TransactionSerializer, BalanceSerializer


class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meetings
        fields = ['room_id', 'room_name', 'is_active', 'created',
                  'user', 'start_date', 'end_date', 'duration','tutor', 'course']

