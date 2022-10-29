from django.urls import path
from .views import  ControleView, Leitura2View, Leitura2Update

urlpatterns = [ 
       
    path('controle/', ControleView.as_view(), name='controle'),
    path('leitura/listar', Leitura2View.as_view(), name='leitura-lista'),
    path('leitura/atualizar/<int:pk>/', Leitura2Update.as_view(), name='leitura-atualizar'),


    

]