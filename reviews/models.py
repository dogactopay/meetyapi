from logging import RootLogger
from django.db import models
from denemeapp.models import Users
import uuid
from datetime import datetime
from django.utils import timezone


ROLES = (
    ("ADMIN", "Admin"),
    ("USER", "User"),
    ("MANAGER", "Manager"),
    ("TUTOR", "Tutor"),

)


class Review(models.Model):
    user_reviews_from = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='user_reviews_from', blank=True)
    user_reviews_to = models.ForeignKey(
        Users, on_delete=models.CASCADE,  related_name='user_reviews_to', blank=True)
        
    created = models.DateTimeField(auto_now_add=True)
    review_id = models.AutoField(primary_key=True)
    review_text = models.TextField(max_length=100, default="")
    review_score = models.DecimalField(
        max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return str(self.user_reviews_to)

    class Meta:
        ordering = ['created']
