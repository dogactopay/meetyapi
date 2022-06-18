from denemeapp.views import UserViewSet
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('users/', include("denemeapp.urls")),
    path('reviews/', include("reviews.urls")),
    path('tangible/', include("tangible.urls")),
    path('admin/', admin.site.urls),
]