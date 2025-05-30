from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.urls.conf import include

from armstrong import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)