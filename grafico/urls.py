from django.urls import path
from .views import GraficoList


urlpatterns = [    
    path('grafico/',GraficoList.as_view() , name="grafico" ),
]