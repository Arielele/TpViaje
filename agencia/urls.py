from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.contrib.staticfiles.urls import static

from agencia.views import bienvenida, login_view, logout_view, register_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('viajes/', include('viajes.urls')),
    path('', bienvenida, name='Bienvenida'),
    path('accounts/login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
