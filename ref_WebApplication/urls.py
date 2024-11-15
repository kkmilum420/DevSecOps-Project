"""ref_WebApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from VolvoVehicleOrder import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from VolvoVehicleOrder.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register('data', searchAndDisplay, basename='data')
#urlpatterns = router.urls

schema_view = get_schema_view(
    openapi.Info(
        title="VehicleOrder",
        default_version='v1',
        description="API for Creating and Maintaining Vehicle Orders",
        terms_of_service="https://www.vehicleorder.com/terms/",
        contact=openapi.Contact(email="kamala.sahoo@volvo.com"),
        license=openapi.License(name="KKS License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.searchAndDisplay, name="searchAndDisplay"),
    path("modify/<str:orderNo>/", views.modifyVehicleOrder, name="modifyVehicleOrder"),
    path("Cancel/<str:orderNo>/", views.deleteVehicleOrder, name="deleteVehicleOrder"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico'))),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
