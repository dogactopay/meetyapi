
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import status
import datetime


class ReviewViewSet(viewsets.ViewSet):

    serializer_class = ReviewSerializer

    def list(self, request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     tutor = get_object_or_404(Tutor.objects.all(), pk=pk)
    #     user_details = get_object_or_404(Users.objects.all(), pk=pk)
    #     serialized_user_details = UserSerializer(user_details)
    #     serializer_tutor = TutorSerializer(tutor)
    #     return Response({**serialized_user_details.data, **serializer_tutor.data})

    # def create(self, request, *args, **kwargs):
    #     serializer = TutorSerializer(data=request.data)
    #     Users.objects.filter(pk=request.data['user']).update(role='TUTOR')
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
