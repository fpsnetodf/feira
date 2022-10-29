from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from .models import Bancas, Leitura, ContaTotal
from django.urls import reverse_lazy

# Create your views here.

################# TemplateView #########################################

class BancaView(TemplateView):
    model = Bancas
    template_name = 'feira/index.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Bancas"
        return context

class LeituraView(TemplateView):
    model = Leitura
    template_name = 'feira/index.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Leituras"

        return context


################# CreateView #########################################

class BancaCreate(CreateView):
    model = Bancas
    fields = '__all__'
    template_name = 'feira/form.html'
    success_url = reverse_lazy('leitura')

class LeituraCreate(CreateView):
    model = Leitura
    fields = '__all__'
    template_name = 'feira/form.html'
    success_url = reverse_lazy('leitura')

class ContaCreate(CreateView):
    model = ContaTotal
    fields = '__all__'
    template_name = 'feira/form.html'
    success_url = reverse_lazy('leitura')


############ ListView ################################################

class BancaList(ListView):
    model = Bancas
    queryset = Bancas.objects.all()
    template_name = 'feira/bancas_list.html'    

class LeituraList(ListView):
    model = Leitura
    queryset = Leitura.objects.all()
    template_name = 'feira/leitura_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conta = ContaTotal.objects.all()
        context['conta'] = conta        
        return context
    
    
    

############# UpdateView ########################################

class BancaUpdate(UpdateView):
    model = Bancas
    fields = '__all__'
    template_name = 'feira/form.html'
    success_url = reverse_lazy('leitura')

class LeituraUpdate(UpdateView):
    model = Leitura
    fields = '__all__'
    template_name = 'feira/form.html'
    success_url = reverse_lazy('leitura')

class ContaUpdate(UpdateView):
    model = ContaTotal
    fields = '__all__'
    template_name = 'feira/form.html'
    success_url = reverse_lazy('leitura')

class HTMX(TemplateView):
    template_name = "feira/htmx_teste.html"
    

class ControleView(ListView):
    model = Leitura
    queryset = Leitura.objects.all()
    template_name = 'feira/Controle.html'