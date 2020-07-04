"""open_neighborhood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from neighborhood import views

# urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('neighborhood_statistics/', include('neighborhood_statistics.urls')),
#    path('neighborhood/', include('neighborhood.urls')),
#    path('aliquots/', include('aliquots.urls')),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^neighborhood/', include('neighborhood.urls')),
    url(r'^neighborhood_statistics/', include('neighborhood_statistics.urls')),
    url(r'^aliquots/', include('aliquots.urls')),
    url(r'^admin/', admin.site.urls),
]
