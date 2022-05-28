from unicodedata import name
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from  rest_framework import routers


from  apps.contas_a_pagar.api.viewsets import Contas_Pagar_viewsets
from apps.fornecedor.api.viewsets import Fornecedor_viresets
from apps.notafiscal.api.viewsets import Nota_Fiscal_viewsets
# ROTAS
router = routers.DefaultRouter()
router.register(r'contas_a_pagar', Contas_Pagar_viewsets)
router.register(r'fornecedor', Fornecedor_viresets)
router.register(r'notafiscal', Nota_Fiscal_viewsets)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('apps.frontend.urls')),
    #path('api/', include('apps.fornecedor.urls')),
    #path('api/', include('apps.notafiscal.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)