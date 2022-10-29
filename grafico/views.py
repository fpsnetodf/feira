from django.views.generic import TemplateView

# Create your views here.

class GraficoList(TemplateView):
    template_name = 'grafico/grafico.html'

