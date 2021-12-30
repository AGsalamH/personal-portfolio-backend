from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

from .models import Project
from .serializers import ProjectSerializer


@api_view()
def projects(request):
    qs = Project.objects.prefetch_related(
        'technologies').select_related('category').all()
    serializer = ProjectSerializer(qs, many=True)
    return Response(serializer.data)
