from rest_framework import serializers
from .models import Users, Meetings, Tutor


class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meetings
        fields = ['room_id', 'room_name', 'is_active', 'created', 'user', 'start_date','end_date','duration']
    
class TutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        fields = ['hourly_price','score','user']
        

class UserSerializer(serializers.ModelSerializer):
    user_meetings = MeetingSerializer(read_only=True, many=True)
    tutor = TutorSerializer(read_only=True)

    class Meta:
        model = Users

        fields = ['user_id','username', 'role','user_meetings','tutor']


