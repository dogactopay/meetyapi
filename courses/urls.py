from .views import CategoryViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'', CategoryViewSet, basename='category')
urlpatterns = router.urls
