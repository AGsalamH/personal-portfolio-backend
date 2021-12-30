from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Social, Education, Resume
from .serializers import (
    SocialSerializer,
    EducationSerializer,
    ResumeSerializer
)


@api_view()
def all(request):
    socialSerializer = SocialSerializer(Social.objects.all(), many=True)
    educationSerializer = EducationSerializer(Education.objects.all(), many=True)
    resumeSerializer = ResumeSerializer(Resume.objects.all(), many=True)

    return Response(data={
        'socials': socialSerializer.data,
        'education': educationSerializer.data,
        'resume': resumeSerializer.data,
    })


@api_view()
def socials(request):
    serializer = SocialSerializer(Social.objects.all(), many=True)
    return Resume(serializer.data)


@api_view()
def resume(request):
    serializer = ResumeSerializer(Resume.objects.all(), many=True)
    return Response(serializer.data)


@api_view()
def education(request):
    serializer = EducationSerializer(Education.objects.all(), many=True)
    return Response(serializer.data)
