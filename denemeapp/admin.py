from django.contrib import admin
from .models import Users, Meetings, Tutor

# Register your models here.


admin.site.register(Users)
admin.site.register(Meetings)
admin.site.register(Tutor)