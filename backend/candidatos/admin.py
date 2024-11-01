from django.contrib import admin
from candidatos.models import DadosPessoais, FormacaoAcademica, Contato, Experiencia, Habilidade, Curriculo

class DadosPessoaisAdmin(admin.ModelAdmin):
    list_display = ('id','nome','email','cpf','data_nascimento')
    list_display_links = ('id','nome',)
    list_per_page = 20
    search_fields = ('nome', 'cpf',)
    ordering = ('nome',)

admin.site.register(DadosPessoais, DadosPessoaisAdmin)

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','telefone','logradouro')
    search_fields = ('cep',)

admin.site.register(Contato,ContatoAdmin)

class FormacaoAcademicaAdmin(admin.ModelAdmin):
    list_display = ('id','universidade','curso','periodo')
    list_display_links = ('id',)

admin.site.register(FormacaoAcademica,FormacaoAcademicaAdmin)

class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('id','empresa','funcao','inicio_data','fim_data')
    list_display_links = ('id','empresa',)
    search_fields = ('empresa',)
    
admin.site.register(Experiencia,ExperienciaAdmin)

class CurriculoAdmin(admin.ModelAdmin):
    list_display = ('id','dados_pessoais','contato')
    list_display_links = ('id','dados_pessoais',)
    search_fields = ('dados_pessoais__nome','contato__telefone')

admin.site.register(Curriculo,CurriculoAdmin)

class HabilidadeAdmin(admin.ModelAdmin):
    list_display = ('id','estudante_nome')
    list_display_links = ('id','estudante_nome')
    search_fields = ('estudante__nome',)

admin.site.register(Habilidade,HabilidadeAdmin)