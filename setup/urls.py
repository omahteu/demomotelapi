from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from produtos.views import ProdutoViewSets
from ig.views import IgViewSets
from camareira.views import CamareiraViewSet
from emeil.views import EmeilViewSet
from quartos.views import QuartoViewSet
from ocupacoes.views import OcupacaoViewSet
from index.views import DadosViewSet
from comanda.views import ComandaViewSet
from patio.views import PatioViewSet
from usuarios.views import UsuarioViewSet
from caixa.views import CaixaViewSet
from painel.views import PainelViewSet
from infos.views import InfosViewSet
from credito.views import CreditoViewSet
from debito.views import DebitoViewSet
from preco.views import TabelaPrecoViewSet
from tempos.views import TemposViewSet
from limpeza.views import LimpezaViewSet
from desistencia.views import DesistenciaViewSet
from valor.views import ValoresViewSet
from auditoria.views import AuditoriaViewSet

router = routers.DefaultRouter()
router.register('caixa', CaixaViewSet, basename='caixa')
router.register('camareiras', CamareiraViewSet, basename='camareira')
router.register('credito', CreditoViewSet, basename='credito')
router.register('comanda', ComandaViewSet, basename='comanda')
router.register('debito', DebitoViewSet, basename='debito')
router.register('dados', DadosViewSet, basename='dados')
router.register('emails', EmeilViewSet, basename='email')
router.register('igs', IgViewSets, basename='ig')
router.register('infos', InfosViewSet, basename='infos')
router.register('ocupacoes', OcupacaoViewSet, basename='ocupacao')
router.register('painel', PainelViewSet, basename='painel')
router.register('patio', PatioViewSet, basename='patio')
router.register('tabela', TabelaPrecoViewSet, basename='tabela')
router.register('produtos', ProdutoViewSets, basename='produtos')
router.register('quartos', QuartoViewSet, basename='quarto')
router.register('tempos', TemposViewSet, basename='tempos')
router.register('usuarios', UsuarioViewSet, basename='usuario')
router.register('limpeza', LimpezaViewSet, basename='limpeza')
router.register('desistencia', DesistenciaViewSet, basename='desistencia')
router.register('valores', ValoresViewSet, basename='valores')
router.register('auditoria', AuditoriaViewSet, basename='auditoria')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
