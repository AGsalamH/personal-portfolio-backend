from rest_framework import serializers
from .models import (
    Education,
    Social,
    Resume
)


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('id', 'name', 'link', 'icon')


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('id', 'university', 'college', 'department',
                  'overview', 'grade', 'graduated_in', 'joined_in'
                  )


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'name', 'job_title', 'bio', 'personal_picture')
