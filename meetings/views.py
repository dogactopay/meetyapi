from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Meetings
from .serializers import MeetingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import Tutor, Users
from rest_framework import permissions
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import status
import datetime
from tangible.ops import show_balance, new_transaction
from meetings.ops import check_availabilty, dateStr2Date, duration


class MeetingsViewSet(viewsets.ViewSet):

    serializer_class = MeetingSerializer

    def list(self, request):
        queryset = Meetings.objects.all()
        serializer = MeetingSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Meetings.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = MeetingSerializer(user)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = MeetingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        parsed_request = (request.data).dict()
        tutor_user_id = (list(Tutor.objects.filter(
            pk=(request.data).dict()['tutor']).values())[0])

        meeting_duration = (duration(dateStr2Date((request.data).dict()['end_date']), dateStr2Date(
            (request.data).dict()['start_date'])))

        meeting_cost = meeting_duration * tutor_user_id['hourly_price']


        exlcuded_users = ([int(i) for i in request.data.getlist("user") if int(i) != int(tutor_user_id['user_id'])])

        user_instance = Users.objects.get(
            pk=int(exlcuded_users[0]))

        user_current_balance = (show_balance(
            int(exlcuded_users[0])))

        #print(check_availabilty(request))

        if 1:
            if user_current_balance >= meeting_cost:
                if check_availabilty(request):
                    new_transaction(user_instance, -meeting_cost,
                                    "Meeting Payment")

                    #Meetings.objects.create(user= tutor_user_id)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"message": "Not available"})
            else:
                return Response({"message": "Not enough balance"})
        else:
            return Response({"message": "Tutor can not be participant"})
