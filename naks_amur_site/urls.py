"""naks_amur_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
import mainapp.views as mainapp
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.index, name='index'),
    path('news/', mainapp.news, name='news'),
    path('details/<slug:pk>', mainapp.details, name='details'),
    path('svarshik/', mainapp.svarshik, name='svarshik'),
    path('doc/', mainapp.doc, name='doc'),
    path('reestr/', mainapp.reestr, name='reestr'),
    path('political/', mainapp.political, name='political'),
    path('svarproizvodstva/', mainapp.svarproizvodstva, name='svarproizvodstva'),
    path('atestatechonlogy/', mainapp.atestatechonlogy, name='atestatechonlogy'),
    path('atestatsvaroborud/', mainapp.atestatsvaroborud, name='atestatsvaroborud'),
    path('contact/', mainapp.contact, name='contact'),
    path('center/', mainapp.center, name='center'),
    path('profstandard/', mainapp.profstandard, name='profstandard'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)