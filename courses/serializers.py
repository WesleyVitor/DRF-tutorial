from dataclasses import field, fields
from rest_framework import serializers

from .models import Course, Avaliation

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = (
            'id',
            'active',
            'created',
            'updated',
            'title',
            'url'
        )


class AvaliationSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kargs = {
            'email': {
                'write_only': True
            }
        }
        model = Avaliation
        fields = (
            'id',
            'active',
            'created',
            'updated',
            'course',
            'name',
            'email',
            'comments',
            'avaliation'
        )