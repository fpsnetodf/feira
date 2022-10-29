from django.urls import path
from .views import BancaView, LeituraView
from .views import LeituraCreate, BancaCreate
from .views import LeituraList, BancaList
from .views import LeituraUpdate, BancaUpdate
from .views import HTMX
from .views import ContaCreate, ContaUpdate, ControleView

urlpatterns = [    
    path('banca/', BancaView.as_view(), name="banca" ),
    path('leitura/',LeituraView.as_view(), name='leitura'),
    path('controle/', ControleView.as_view(), name='controle'),
    
    path('criar/leitura/',LeituraCreate.as_view(), name='criar_leitura'),
    path('criar/banca/',BancaCreate.as_view(), name='criar_banca'),

    path('listar/leitura/',LeituraList.as_view(), name='listar_leitura'),
    path('listar/banca/',BancaList.as_view(), name='listar_banca'),

    path('atualizar/leitura/<int:pk>',LeituraUpdate.as_view(), name='atualizar_leitura'),
    path('atualizar/banca/<int:pk>',BancaUpdate.as_view(), name='atualizar_banca'),
    path("htmx/", HTMX.as_view(), name="htmx"),
    # Conta #
    path("conta/create/", ContaCreate.as_view(), name="conta-create"),
    path("conta/update/<int:pk>", ContaUpdate.as_view(), name="conta-update"),
]