from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os  # Needed for os.path.join

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'carEra', 'static'))
