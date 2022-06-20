from rest_framework import serializers
from .models import Category, Course

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course

        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    course_category_name = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Category

        fields = ['category_name','course_category_name']


