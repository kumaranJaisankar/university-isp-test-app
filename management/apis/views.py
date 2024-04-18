from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from openwisp_radius.models import RadiusPostAuth
from rest_framework.permissions import IsAuthenticated
from management.apis.serializers import RadAuthSerilizers


class GetRadLogAuth(RetrieveUpdateDestroyAPIView):
    # for testing
    queryset =RadiusPostAuth.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = RadAuthSerilizers
    lookup_field= 'username'





