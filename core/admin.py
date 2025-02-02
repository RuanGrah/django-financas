from django.contrib import admin

from django.contrib.admin import AdminSite

from .models import Categoria, Conta , LancamentoFinanceiro

# Register your models here.

class LancamentoAdmin(admin.ModelAdmin):
    list_display = ("data", "historico" ,"credito_debito",  "valor")


admin.site.register(Categoria)
admin.site.register(Conta)
admin.site.register(LancamentoFinanceiro, LancamentoAdmin)

# Alteracoes visuais

admin.site.site_header = "Projeto Finanças"
admin.site.site_title = "Site Finanças"
admin.site.index_title = "Bem-vindo ao Projeto Finanças"

