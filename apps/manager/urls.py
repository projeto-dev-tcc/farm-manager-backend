from manager.views import DetailFazenda, ListFazenda
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
    path('api/fazendas/', ListFazenda),
    path('api/fazendas/<int:pk>', DetailFazenda),
    # path('', include(router.urls)),
]

