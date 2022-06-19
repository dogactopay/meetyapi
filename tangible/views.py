
from .models import Transaction, Balance
from users.models import Users
from .serializers import BalanceSerializer, TransactionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import status
import datetime
from django.forms.models import model_to_dict


class TransactionViewSet(viewsets.ViewSet):

    serializer_class = TransactionSerializer

    def list(self, request):
        queryset = Transaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = TransactionSerializer(data=request.data)
        req_user = Users.objects.get(pk=request.data['user'])

        try:
            current_bal = Balance.objects.filter(
                user_balance=req_user).values()[0]['balance']

        except:
            current_bal = ""

        print(current_bal)

        if len(str(current_bal)) > 0:
            Balance.objects.filter(user_balance=req_user).update(
                balance=float(current_bal) + float(dict(**request.data)['amount'][0]))
        else:
            print("acıl")
            Balance.objects.create(user_balance=req_user, balance=float(
                dict(**request.data)['amount'][0]))

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BalanceViewSet(viewsets.ViewSet):

    serializer_class = BalanceSerializer

    def list(self, request):
        queryset = Balance.objects.all()
        serializer = BalanceSerializer(queryset)
        return Response(serializer.data)
