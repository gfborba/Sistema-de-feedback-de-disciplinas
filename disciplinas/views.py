from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Disciplina

@login_required(login_url='login')
def index(request):

    disciplinas = Disciplina.objects.all
