from django.contrib import admin
from .models import Bancas, Leitura, ContaTotal

# Register your models here.
admin.site.register(Bancas)
admin.site.register(Leitura)
admin.site.register(ContaTotal)

