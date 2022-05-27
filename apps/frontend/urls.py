
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from fornecedor.views import import_csv, export_csv, upload_file_view
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('import/', import_csv, name='import_csv'),
    path('export/', export_csv, name='export_csv'),
    path('upload-file/', upload_file_view, name='upload_csv'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)