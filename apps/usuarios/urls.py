from manager.viewsets import *
from django.urls import path, include
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)