# https://docs.djangoproject.com/en/5.1/topics/http/urls/

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from app.views.site import landing

urlpatterns = [
    path("", landing),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
