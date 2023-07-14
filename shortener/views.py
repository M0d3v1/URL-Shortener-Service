from rest_framework import generics
from .models import URL
from .serializers import URLSerializer


class URLListCreateAPIView(generics.ListCreateAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer


class URLRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
