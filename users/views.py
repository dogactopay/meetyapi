from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from courses.models import Course
from rest_framework.parsers import JSONParser
from .models import Users, Tutor, Purchased_Course
from meetings.models import Meetings
from .serializers import TutorSerializer, UserSerializer, PurchasedCourseSerializer
from meetings.serializers import MeetingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import status
import datetime
from meetings.ops import check_availabilty, dateStr2Date, duration
from tangible.ops import show_balance, new_transaction


class UserViewSet(viewsets.ViewSet):

    serializer_class = UserSerializer

    def list(self, request):
        queryset = Users.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Users.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["get"], url_path=r'is-active-meeting',)
    def User_Active_Meeting(self, request, pk=None):
        data = Meetings.objects.filter(user=pk).filter(
            start_date__lte=datetime.datetime.now()).filter(end_date__gte=datetime.datetime.now())
        serializer = MeetingSerializer(data, many=True)
        return Response(serializer.data)


class TutorViewSet(viewsets.ViewSet):

    serializer_class = TutorSerializer

    def list(self, request):
        queryset = Users.objects.filter(role='TUTOR')
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        tutor = get_object_or_404(Tutor.objects.all(), pk=pk)
        user_details = get_object_or_404(Users.objects.all(), pk=pk)
        serialized_user_details = UserSerializer(user_details)
        serializer_tutor = TutorSerializer(tutor)
        return Response({**serialized_user_details.data, **serializer_tutor.data})

    def create(self, request, *args, **kwargs):
        serializer = TutorSerializer(data=request.data)
        Users.objects.filter(pk=request.data['user']).update(role='TUTOR')
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PurchasedCourseViewSet(viewsets.ViewSet):

    serializer_class = PurchasedCourseSerializer

    def list(self, request):
        queryset = Purchased_Course.objects.all()
        serializer = PurchasedCourseSerializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     tutor = get_object_or_404(Tutor.objects.all(), pk=pk)
    #     user_details = get_object_or_404(Users.objects.all(), pk=pk)
    #     serialized_user_details = UserSerializer(user_details)
    #     serializer_tutor = TutorSerializer(tutor)
    #     return Response({**serialized_user_details.data, **serializer_tutor.data})

    def create(self, request, *args, **kwargs):
        serializer = PurchasedCourseSerializer(data=request.data)

        parsed_request = (request.data).dict()

        user_instance = Users.objects.get(
            pk=int(parsed_request['purchased_user']))

        user_current_balance = (show_balance(
            int(parsed_request['purchased_user'])))

        course_instance = list(Course.objects.filter(
            pk=int(parsed_request['purchased_course'])).values())[0]

        if user_current_balance >= course_instance['course_price']:
            
            new_transaction(user_instance, -course_instance['course_price'], "Meeting Payment")

            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Not Enough Balance"})
