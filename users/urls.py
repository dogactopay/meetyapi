from .views import UserViewSet, TutorViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'tutors', TutorViewSet, basename='tutors')
urlpatterns = router.urls
