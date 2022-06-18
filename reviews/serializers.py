from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):


    class Meta:
        model = Review

        fields = ['user_reviews_from','user_reviews_to','review_text','review_score']


