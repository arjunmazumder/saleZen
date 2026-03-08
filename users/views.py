from django.shortcuts import render

from rest_framework import generics
from users.models import Designation
from users.serializers import DesignationSerializer

class DesignationListCreateView(generics.ListCreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


