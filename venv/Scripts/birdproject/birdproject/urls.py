from django.contrib import admin
from django.urls import path, include
from birbs.views import index  # Import the new view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index),  # Root URL
    path('admin/', admin.site.urls),
    path('api/', include('birbs.urls')),  # Include the app's URLs
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
