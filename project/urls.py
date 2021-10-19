from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # INCLUDE APPS
    path('', include('home.urls')),
    path('', include('manager.urls')),
    path('', include('usuarios.urls')),
    
    # ARCHIVES STATIC's
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
