"""CKYC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('',include('details.urls',namespace ="details")),
    path('',include('UserProfile.urls',namespace ="userprofile")),
    path('',include('workflow.urls',namespace ="workflow")),



    url(r'^form/temp.js/$',views.js,name='js'),
    url(r'^mod_form/addform.js/$',views.addform,name='addform'),
    url(r'^check_did1/updateform1/update.js/$',views.updateform,name='updateform'),
    path('first',views.first,name="first")
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)