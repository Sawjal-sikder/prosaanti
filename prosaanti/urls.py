from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('super/admin/', admin.site.urls),
    path('admin/', include('dashboard.urls')),
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]