from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manager.urls')),
    path('auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]