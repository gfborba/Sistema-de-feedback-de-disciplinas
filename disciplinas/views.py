from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Disciplinas, Avaliacao

@login_required(login_url='login')
def index(request):

    disciplinas = Disciplinas.objects.all
    return render(request, 'index.html', {'disciplinas':disciplinas})

def disciplinas(request, id):
    disciplinas = Disciplinas.objects.get(id=id)
    return render (request, 'disciplinas.html', {'disciplinas':disciplinas})

def avaliacao(request, id):
    disciplina = Disciplinas.objects.get(id=id)
    avaliacao_aluno = Avaliacao.objects.filter(disciplina=disciplina, user=request.user)

    if avaliacao_aluno.exists():
            return HttpResponse ("Você já avaliou essa disciplina!")
    else:
        if request.method == "POST":
                nota = request.POST.get('nota')
                comentario = request.POST.get('comentario')

                avaliacao = Avaliacao.objects.create(
                    disciplina=disciplina,
                    user=request.user,
                    nota=nota,
                    comentario=comentario)
                avaliacao.save()
                return HttpResponse("Avaliação realizada com sucesso.")
        else:
            return render (request, 'avaliar.html',{'disciplina':disciplina})
