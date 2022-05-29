
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from fornecedor.views import (
    import_csv, export_csv, 
    all_fornecedores, FornecedorEdit,
    FornecedorCreate, FornecedorDelete
    )
from notafiscal.views import (
    notas_fiscais, NotasFiscaisCreate, 
    export_notas_csv)

from user.views import (
    LoginView, LogoutView,
    SignUpView, profileView,
    ProfileUpdateView
)

from .views import index


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('profile/', profileView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),

    path('', index, name='index'),
    path('import/', import_csv, name='import_csv'),
    path('export/', export_csv, name='export_csv'),
    path('upload-file/', all_fornecedores, name='all_fornecedores'),

    path('editar-fornecedor/<str:pk>/', FornecedorEdit.as_view(), name='FornecedorEdit'),
    path('criar-fornecedor/', FornecedorCreate, name='Create_Fornecedor'),
    path('deletar-fornecedor/<str:pk>/', FornecedorDelete.as_view(), name='FornecedorDelete'),

    path('notas-fiscais/', notas_fiscais, name='notas_fiscais'),
    path('cadastrar-fiscais/', NotasFiscaisCreate, name='NotasFiscaisCreate'),
    path('export-fiscais/', export_notas_csv, name='export_notas_csv'),


]

# Para carregar STATIC e as MIDIAS
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)