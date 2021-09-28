from django.contrib import admin
from django.urls import path, include

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manager.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]