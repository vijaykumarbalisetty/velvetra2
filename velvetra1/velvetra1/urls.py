"""
URL configuration for velvetra1 project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('velvetra2.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve the React frontend's index.html for ALL other routes
# This makes http://127.0.0.1:8000/ and any SPA routes work
urlpatterns += [
    re_path(r'^(?!api/|admin/|media/|static/).*$', TemplateView.as_view(template_name='index.html'), name='react-frontend'),
]
