from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UsuarioSerializer
from .models import Usuarios


# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer



