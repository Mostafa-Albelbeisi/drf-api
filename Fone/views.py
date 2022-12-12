from django.shortcuts import render

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import FoneSerializer

# Create your views here.
from .models import Fone


class FoneListView(ListCreateAPIView):
    queryset = Fone.objects.all()
    serializer_class = FoneSerializer


class FoneDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Fone.objects.all()
    serializer_class = FoneSerializer
