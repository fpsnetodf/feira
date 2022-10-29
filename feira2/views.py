from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from feira.models import  Leitura, Bancas
from django.urls import reverse_lazy
# controle de login
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ControleView(ListView):
    model = Leitura
    queryset = Leitura.objects.all()
    template_name = 'feira/Controle.html'

class Leitura2View(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Leitura
    queryset = Leitura.objects.all()
    template_name = 'feira2/Leitura_lista.html' 
    

class Leitura2Update(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Leitura
    queryset = Leitura.objects.all()
    fields = ["banca", "anterior", "atual"]
    template_name = 'feira2/Leitura_update.html'
    success_url = reverse_lazy('leitura-lista')
    def form_valid(self, form):       
        url = super().form_valid(form)
        self.object.anterior = self.object.atual
        self.object.atual += 0
        self.object.save()        
        return url
    

    


