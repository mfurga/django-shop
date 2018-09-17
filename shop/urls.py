from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from .api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('account/', include('users.urls')),
    path('', include('ads.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
