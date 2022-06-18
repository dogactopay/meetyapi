from .views import ReviewViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'', ReviewViewSet, basename='review')
urlpatterns = router.urls
