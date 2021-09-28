from rest_framework import viewsets, serializers, generics, filters
from .models import Musica
from .serializers import MusicaSerializer


# class MusicaViewSet(viewsets.ModelViewSet):
#     serializer_class = MusicaSerializer
#     queryset = Musica.objects.all()

class MusicaListView(viewsets.ModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'cantor', 'compositor', 'album']

class MusicaViewSet(viewsets.ModelViewSet):
    serializer_class = MusicaSerializer

    def get_queryset(self):
        queryset = Musica.objects.all()        
        name = self.request.query_params.get('nome')        
        if name is not None:
            queryset = queryset.filter(nome=name)
        return queryset

# class ItemViewSet(viewsets.ModelViewSet):
#     serializer_class = ItemSerializer

#     def get_queryset(self):
#         return Item.objects.filter(
#             channel=self.kwargs["channel_pk"])