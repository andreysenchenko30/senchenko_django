"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from some_app.views import index, get_information, add_page, add, home_page
from src import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name=''),
    path('view/', get_information, name='get_information'),
    path('add_page/', add_page, name='add_page'),
    path('add/', add, name='add'),
    path('home_page/', home_page, name='home_page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
