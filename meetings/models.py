from logging import RootLogger
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
import uuid
from datetime import datetime
from django.utils import timezone
from users.models import Users, Tutor
from courses.models import Course


def today_utc():
    return datetime.utcnow()


class Meetings(models.Model):
    user = models.ManyToManyField(
        Users, related_name='user_meetings', blank=True)
    course = models.ForeignKey(
        Course, related_name='user_course_meetings', blank=True, null=True, on_delete=models.SET_NULL,  default=None)
    tutor = models.ForeignKey(
        Tutor, related_name='tutor_meetings', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(
        max_length=100, default=uuid.uuid4)
    #is_active = models.BooleanField(default=False)
    start_date = models.DateTimeField(default=today_utc)
    end_date = models.DateTimeField(default=today_utc)

    @property
    def duration(self):
        return round(float(str((self.end_date - self.start_date)/3600).split(":")[2]))

    def __str__(self):
        return self.room_name

    class Meta:
        ordering = ['created']
