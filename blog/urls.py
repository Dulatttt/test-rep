from django.contrib import admin
from django.urls import path, re_path, include
from myapp.views import *
from blog import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    

    path('', include('myapp.urls')),
    
]
handler404=PageNotFound

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)