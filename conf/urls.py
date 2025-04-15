from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('disciplinas.urls')),
    path('auth/', include ('alunos.urls'))
]
