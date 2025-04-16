from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('disciplinas/<int:id>', views.disciplinas, name = 'disciplinas'),
]