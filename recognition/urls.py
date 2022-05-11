from django.contrib import admin
from django.urls import path, include
from recognition import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('test/', views.test_view, name='test'),
    path('test2/', views.model_form_upload, name='test2'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)