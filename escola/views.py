from django.shortcuts import render,redirect
from .models import Aluno
from .forms import AlunoForm




# Create your views here.
def index(request):
        alunos = Aluno.objects.all()
        return render(request, 'escola/index.html', {'alunos': alunos})


def cadastrar(request):
        if request.method == 'POST':
                form = AlunoForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save()
                        return redirect('index')
        else:
                form = AlunoForm()
        
        return render(request, 'escola/cadastro_aluno.html', {'form': form})

 
def editar(request, id):
        aluno = Aluno.objects.get(id=id)
        form = AlunoForm(instance=aluno)
        if (request.method == 'POST'):
                form = AlunoForm(request.POST, request.FILES, instance=aluno)
                if form.is_valid():
                        form.save()
                        return redirect('index')
        else:
                form = AlunoForm(instance=aluno)
        
        return render(request, 'escola/cadastro_aluno.html', {'form': form})


def deletar(request, id):
        Aluno.objects.get(id=id).delete()
        return redirect('index')
