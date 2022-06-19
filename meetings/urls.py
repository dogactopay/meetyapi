from .views import MeetingsViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'meetings', MeetingsViewSet, basename='meeting')
urlpatterns = router.urls
