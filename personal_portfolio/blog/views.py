from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
# Create your views here.


@api_view()
def posts(request):
    qs = Post.objects.select_related('creator').all()
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)
