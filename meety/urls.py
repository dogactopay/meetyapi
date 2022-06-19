
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('users/', include("users.urls")),
    path('reviews/', include("reviews.urls")),
    path('tangible/', include("tangible.urls")),
    path('users/', include("users.urls")),
    path('meetings/', include("meetings.urls")),
    path('courses/', include("courses.urls")),
    path('admin/', admin.site.urls),
]