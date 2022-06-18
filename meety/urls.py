from denemeapp.views import UserViewSet
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/', include("denemeapp.urls")),
    path('admin/', admin.site.urls),
]