from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from authorization.views import GetToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tours/', include('tours.urls')),
    path(r'^auth/', include('djoser.urls')),
    path('check_token/', GetToken.as_view()),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
