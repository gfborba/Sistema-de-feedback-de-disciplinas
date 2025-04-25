from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Disciplinas, Avaliacao
from django.db.models import Avg

@login_required(login_url='login')
def index(request):
    disciplinas = Disciplinas.objects.annotate(media=Avg('avaliacao__nota')).all()
    return render(request, 'index.html', {'disciplinas': disciplinas})

def disciplinas(request, id):
    disciplina = get_object_or_404(
        Disciplinas.objects.annotate(media=Avg('avaliacao__nota')), id=id
    )
    return render(request, 'disciplinas.html', {'disciplinas': disciplina})

@login_required(login_url='login')
def avaliacao(request, id):
    disciplina = get_object_or_404(Disciplinas, id=id)
    ja_avaliou = Avaliacao.objects.filter(
        disciplina=disciplina,
        user=request.user
    ).exists()

    if ja_avaliou:
        return render(request, 'disciplinas.html', {
            'disciplinas': disciplina, 'alreadyav': 'Avaliação já realizada para essa disciplina'
        })

    if request.method == "POST":
        nota = request.POST.get('nota')
        comentario = request.POST.get('comentario')
        Avaliacao.objects.create(
            disciplina=disciplina,
            user=request.user,
            nota=nota,
            comentario=comentario
        )
        return render(request, 'disciplinas.html', {'disciplinas': disciplina})
    else:
        return render(request, 'avaliar.html', {'disciplina': disciplina})
