"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from projeto.produto.views.produto_viewset import ProdutoViewSet
from projeto.produto.views.categoria_viewset import CategoriaViewSet
from projeto.estoque.views.estoque_entrada_viewset import EstoqueEntradaViewSet
from projeto.estoque.views.estoque_saida_viewset import EstoqueSaidaViewSet

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r'estoque-entrada', EstoqueEntradaViewSet)
router.register(r'estoque-saida', EstoqueSaidaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
