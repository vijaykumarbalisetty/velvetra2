from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'designers', views.DesignerViewSet)
router.register(r'projects', views.DesignProjectViewSet)

urlpatterns = [
    path('', include(router.urls)), # type: ignore
    path('core/upload/', views.upload_file, name='upload_file'),
    path('core/generate/', views.generate_image, name='generate_image'),
]
