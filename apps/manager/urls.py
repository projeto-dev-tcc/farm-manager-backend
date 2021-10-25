from manager.views import *
from django.urls import path
from rest_framework import routers

urlpatterns = [
    # FAZENDA
    # path('api/fazendas/', ListFazenda),
    # path('api/fazendas/<int:pk>', DetailFazenda),
    
    # VARIEDADE
    path("registrar/variedade/", registrar_variedade, name="registrar_variedade"),
]

