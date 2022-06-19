from logging import RootLogger
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
import uuid
from datetime import datetime
from django.utils import timezone


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
ROLES = (
    ("ADMIN", "Admin"),
    ("USER", "User"),
    ("MANAGER", "Manager"),
    ("TUTOR", "Tutor"),

)


def today_utc():
    return datetime.utcnow()


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)

    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=True, default='')
    role = models.CharField(choices=ROLES, default='user', max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['created']


class Tutor(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    tutor_id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    hourly_price = models.DecimalField(
        max_digits=5, decimal_places=2, default=0)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ['created']

