from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerilizer

class CrudView(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerilizer