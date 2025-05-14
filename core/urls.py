from django.contrib import admin
from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.permission import IsStaffUserOr404

schema_view = get_schema_view(
   openapi.Info(
      title="Chimgan Water WebSite API",
      default_version='v1',
      description="API documentation for Chimgan Water WebSite",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="xoliqberdiyevbehruz12@gmail.com"),
      license=openapi.License(name="BEHRUZ XOLIQBERDIYEV"),
   ),
   public=True,
   permission_classes=(IsStaffUserOr404,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
