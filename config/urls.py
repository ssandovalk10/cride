from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
   
    path("", include("cride.users.urls", namespace="users")),    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

