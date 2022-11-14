from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
urlpatterns = [
    path('api_schema', get_schema_view(title='API Schema', description='Swag nigger'), name='api_schema'),
    path('api/', include('movies_api.urls')),
    path('admin/', admin.site.urls),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
]
