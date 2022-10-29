from django.db import models

# Create your models here.



class Bancas(models.Model):
    numero = models.IntegerField(unique=True, verbose_name="Número")
    qtd = models.IntegerField(default=1)
    obs = models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
        return f"{self.qtd} - {self.numero} ({self.obs})"
    class Meta:
        ordering = ['numero']

class ContaTotal(models.Model):
    conta = models.FloatField("Conta total", max_length=10)
    kwh = models.FloatField("Kw/h", max_length=5, null=True, blank=True)
    taxaIlum = models.FloatField("Tx iluminação Pública", max_length=5)
    corredor = models.FloatField("Iluminação dos Corredores", max_length=5)
    def __str__(self):
        return f"Valor Total: R$  {self.conta:.2f} Taxa Iluminação: R$ {self.taxaIlum:.2f} Corredor: R$: {self.corredor:.2f}"

class Leitura(models.Model):
    anterior = models.IntegerField(verbose_name='Leitura Anterior')
    atual = models.IntegerField(verbose_name='Leitura Atual')
    data = models.DateTimeField(auto_created=True, auto_now=True)
    banca = models.ForeignKey("Bancas" ,on_delete=models.PROTECT, related_query_name='bancas')
    
    def __str__(self):
        return f"{self.banca.qtd}-Banca: ({self.banca.numero}) - ({self.anterior}-{self.atual}) = [ {self.atual - self.anterior}  Kwh ] R$ {(((self.atual - self.anterior) * 0.75))}- Taxa Iluminação ({self.banca.qtd * 7.50 :.2f})- Area comum ({self.banca.qtd * 8.50}) Total = {((self.atual - self.anterior) * 0.75) + (self.banca.qtd * 7.50) + (self.banca.qtd * 8.50 ):.2f} )"
    class Meta:
        ordering = ['banca']
