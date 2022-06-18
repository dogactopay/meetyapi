from .views import TransactionViewSet, BalanceViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'balance', BalanceViewSet, basename='balance')
urlpatterns = router.urls
