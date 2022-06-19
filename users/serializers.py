from rest_framework import serializers
from .models import Users, Tutor
from meetings.models import Meetings
from meetings.serializers import MeetingSerializer
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from tangible.serializers import TransactionSerializer, BalanceSerializer



class TutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        fields = ['hourly_price', 'score', 'user']


class UserSerializer(serializers.ModelSerializer):
    user_meetings = MeetingSerializer(read_only=True, many=True)
    user_reviews_from = ReviewSerializer(read_only=True, many=True)
    user_reviews_to = ReviewSerializer(read_only=True, many=True)
    user_transaction = TransactionSerializer(read_only=True, many=True)

    tutor = TutorSerializer(read_only=True)
    user_balance = BalanceSerializer(read_only=True)

    class Meta:
        model = Users

        fields = ['user_id', 'username', 'role', 'user_meetings', 'tutor',
                  'user_reviews_from', 'user_reviews_to', 'user_transaction', 'user_balance']
