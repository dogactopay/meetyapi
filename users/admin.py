from django.contrib import admin
from .models import Users, Tutor, Purchased_Course

# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    def get_username(self, obj):
        return obj.user.username

    list_display = ['get_username','hourly_price','score','is_verified']

class PurchasedCourseAdmin(admin.ModelAdmin):
    def get_username(self, obj):
        return obj.purchased_user.username

    def get_course(self, obj):
        return obj.purchased_course.course_name

    list_display = ['get_username','get_course','created']


admin.site.register(Users)
admin.site.register(Tutor, PersonAdmin)
admin.site.register(Purchased_Course,PurchasedCourseAdmin)
