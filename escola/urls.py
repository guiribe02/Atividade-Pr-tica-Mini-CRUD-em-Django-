from django.urls import path
from alunos import views

urlpatterns = [
    path('', views.listar_alunos, name='listar_alunos'),
    path('cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('editar/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('excluir/<int:id>/', views.excluir_aluno, name='excluir_aluno'),
]
