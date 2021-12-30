from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from .models import Contact
from .serializers import ContactSerializer


# Create your views here.
@api_view()
def hire_me(request):
    qs = Contact.objects.all()
    serializer = ContactSerializer(qs, many=True)
    return Response(serializer.data)
