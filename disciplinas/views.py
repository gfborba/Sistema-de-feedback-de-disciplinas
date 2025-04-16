from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Disciplinas

@login_required(login_url='login')
def index(request):

    disciplinas = Disciplinas.objects.all
    return render(request, 'index.html', {'disciplinas':disciplinas})

def disciplinas(request, id):
    disciplinas = Disciplinas.objects.get(id=id)
    return render (request, 'disciplinas.html', {'disciplinas':disciplinas})