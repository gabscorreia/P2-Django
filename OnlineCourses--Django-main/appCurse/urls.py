from . import views
from django.urls import path

urlpatterns = [
    path('', views.appCursos, name="appCursos"),  # Página inicial
    path('cadastro/', views.cadastrar_user, name='cadastrar_user'),  # Cadastro de usuário
    path('cursos/', views.cadastrar_curso, name='cadastrar_curso'),  # Cadastro de cursos
    path('contato/', views.contato, name='contato'),  # Página de contato
    path('listar-cursos/', views.exibir_cursos, name='exibir_cursos'),  # Listagem de cursos
    path('usuarios/', views.exibir_users, name='exibir_usuarios'),  # Listagem de usuários
    path('login/', views.form_login, name='form_login'),  # Formulário de login
    path('dashboard/', views.dashboard, name='dashboard'),  # Painel de controle
    path('editar_usuario/<int:id_usuario>', views.editar_usuario, name='editar_usuario'),  # Edição de usuário
    path('excluir_usuario/<int:id_usuario>', views.excluir_usuario, name='excluir_usuario'),  # Exclusão de usuário
    path('add-foto/', views.add_foto, name='add_foto'),  # Adicionar foto
    path('galeria/', views.galeria, name='galeria'),  # Galeria de fotos
]