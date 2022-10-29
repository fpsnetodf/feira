from django.db import models


# Create your models here.

# bancas = [('01', "590/611"),
#         ('02', "591 "),
#         ("03", "592/594"),
#         ("04","593"),
#         ('05', '595'), 
#         ('06','596/605'),
#         ('07', '597'),
#         ('08', '598'),
#         ('09', '599'),
#         ('10', '600'),
#         ('11', '601/603'),
#         ('12', '602'),        
#         ('13', '604'),
#         ('14', '606'),
#         ('15', '607'),
#         ('16', '608'),
#         ('17', '609'),
#         ('18', '612/610/640/641'),
#         ('19', '613/615'),
#         ('20', '614/616'),
#         ('21', '618/637'),
#         ('22', '626/633'),
#         ('23', '628'),
#         ('24', '630'),
#         ('25', '631'),
#         ('26', '632'),
#         ('27', '635'),
#         ('28', '636'),
#         ('29', '638/639'),
#         ('30', '642'),
#         ('31', '643'),
#         ('32', '644'),
#         ('33', '645'),
#         ('34', '646'),
# ]



# class Leitura2(models.Model):
#     anterior = models.IntegerField("Leitura anterior")
#     atual = models.IntegerField("Leitura atualr")
#     data = models.DateTimeField(auto_created=True, auto_now=True)
#     banca = models.ForeignKey(Banca, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f"{self.banca.qtd}-Banca: ({self.banca}) - ({self.anterior}-{self.atual}) = [ {self.atual - self.anterior}  Kwh ] R$ {(((self.atual - self.anterior)* 0.75)/2) + (self.banca.qtd * 7.851) + (self.banca.qtd * 7.901):.2f} "
    

