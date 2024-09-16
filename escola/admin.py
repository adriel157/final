from django.contrib import admin
from .models import Aluno,Curso

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','data_nascimento','email','curso')
admin.site.register(Aluno,AlunoAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao','vagas','inscritos')
admin.site.register(Curso,CursoAdmin)