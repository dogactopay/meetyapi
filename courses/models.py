from logging import RootLogger
from django.db import models
from users.models import Users, Tutor
import uuid
from datetime import datetime
from django.utils import timezone


class Category(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.category_name)

    class Meta:
        ordering = ['created']


class Course(models.Model):
    course_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='course_category_name', blank=True)
    course_owner = models.ForeignKey(
        Tutor, on_delete=models.CASCADE, related_name='course_owner_name', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.course_name)

    class Meta:
        ordering = ['created']
