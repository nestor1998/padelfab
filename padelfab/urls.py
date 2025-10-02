"""
URL configuration for padelfab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core import views as v_core
from foro import views as v_foro
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v_core.home,name="home"),
    path('noticias/',v_foro.noticias,name="noticias"),
    path('quienessomos/',v_core.quienessomos,name="quienessomos"),
    path('suscribete/',v_core.suscribete,name="suscribete")
]




if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)