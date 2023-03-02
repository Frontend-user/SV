from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
urlpatterns = [
    path('', include('mod.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document__root=settings.STATIC_ROOT)
