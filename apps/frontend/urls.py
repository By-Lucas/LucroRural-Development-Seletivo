from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from fornecedor.views import (
    export_csv, 
    all_fornecedores, FornecedorEdit,
    FornecedorCreate, FornecedorDelete
    )
from notafiscal.views import (
    notas_fiscais, NotasFiscaisCreate, 
    export_notas_csv, NotaUpdateView
    )
from contas_a_pagar.views import (
    contas_pagar_list, ContasPagarDelete,
    contas_pagar_create, ContasUpdateView
    )
from user.views import (
    LoginView, LogoutView,
    SignUpView, profileView,
    ProfileUpdateView
    )
from .views import index


urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('profile/', profileView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),

    path('export-fornecedor/', export_csv, name='export_csv'),
    path('fornecedores/', all_fornecedores, name='all_fornecedores'),
    path('editar-fornecedor/<str:pk>/update/', FornecedorEdit.as_view(), name='FornecedorEdit'),
    path('criar-fornecedor/', FornecedorCreate, name='Create_Fornecedor'),
    path('deletar-fornecedor/<str:pk>/', FornecedorDelete.as_view(), name='FornecedorDelete'),

    path('notas-fiscais/', notas_fiscais, name='notas_fiscais'),
    path('cadastrar-fiscais/', NotasFiscaisCreate, name='NotasFiscaisCreate'),
    path('export-fiscais/', export_notas_csv, name='export_notas_csv'),
    path('nota-fiscal/<pk>/update/', NotaUpdateView.as_view(), name='NotaUpdateView'),

    path('contas-pagar/', contas_pagar_list, name='contas_pagar_list'),
    path('nova-contas-pagar/', contas_pagar_create, name='ContasPagarCreate'),
    path('deletar-contas-pagar/<str:pk>/', ContasPagarDelete.as_view(), name='ContasPagarDelete'),
    path('contas-pagar/<pk>/update/', ContasUpdateView.as_view(), name='ContasUpdateView'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)