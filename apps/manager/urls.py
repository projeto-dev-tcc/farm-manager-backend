from manager.views import *
from django.urls import path
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'fazendas', FazendaViewSet)
# router.register(r'maquinarios', MaquinarioViewSet)
# router.register(r'variedades', VariedadeViewSet)
# router.register(r'talhoes', TalhaoViewSet)
# router.register(r'servicos', ServicoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # FAZENDA
    path('api/fazendas/', ListFazenda),
    path('api/fazendas/<int:pk>', DetailFazenda),
    
    # MAQUINÁRIO
    path('api/maquinarios/', ListMaquinario),
    path('api/maquinarios/<int:pk>', DetailMaquinario),
    
    # SERVIÇO
    path('api/servicos/', ListServico),
    path('api/servicos/<int:pk>', DetailServico),
    
    # TALHÃO
    path('api/talhoes/', ListTalhao),
    path('api/talhoes/<int:pk>', DetailTalhao),
    
    # VARIEDADE
    path('api/variedade/', ListVariedade),
    path('api/variedade/<int:pk>', DetailVariedade),
    
    # path('', include(router.urls)),
]

