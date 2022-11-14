from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include # url()


from django.views.decorators.csrf import csrf_exempt


from t_messages.views import (
    home_view, feed_view, search_view
)
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from accounts.views import (
    login_view,
    logout_view,
    register_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view),
    path('feed/', feed_view),
    path('search/', search_view),
    
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),

    re_path(r'^profiles?/', include('profiles.urls')),
    re_path(r'^threads?/', include('threads.urls')),

    re_path(r'^api/profiles?/', include('profiles.api.urls')),
    re_path(r'^api/messages?/', include('t_messages.api.urls')),
    re_path(r'^api/threads?/', include('threads.api.urls')),

    path('api_schema', get_schema_view(title='API Schema', description='Swag nigger'), name='api_schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)