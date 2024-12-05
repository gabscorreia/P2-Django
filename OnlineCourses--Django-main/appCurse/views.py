from datetime import timedelta
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from appCurse.models import Usuario, Curso, Foto
from appCurse.forms import FormLogin, FormCadastroUser, FormCadastroCurso, FormEditarUsuario, FormFoto

def appCurse(request):
    return render(request, 'index.html')

def cadastrar_user(request):
    novo_user = FormCadastroUser(request.POST or None, request.FILES or None)
    if request.POST:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "E-mail já está sendo utilizado!")
        elif novo_user.is_valid():
            novo_user.instance.senha = make_password(senha)
            novo_user.save()
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect('appCurse')
    context = {'form': novo_user}
    return render(request, 'cadastro.html', context)

def exibir_users(request):
    email = request.session.get('email')

    if not email:
        messages.error(request, "Você precisa estar logado para acessar a lista de usuários!")
        return redirect('form_login')

    usuarios = Usuario.objects.all().values()
    context = {'dados': usuarios}
    return render(request, 'usuarios.html', context)

def exibir_cursos(request):
    cursos = Curso.objects.all().values()
    context = {'dados': cursos}
    return render(request, 'cursos.html', context)

def cadastrar_curso(request):
    novo_curso = FormCadastroCurso(request.POST or None, request.FILES or None)
    if request.POST:
        if novo_curso.is_valid():
            novo_curso.save()
            messages.success(request, "Curso adicionado com sucesso!")
            return redirect('appCurse')
    context = {'form': novo_curso}
    return render(request, 'biblioteca.html', context)

def form_login(request):
    formLogin = FormLogin(request.POST or None)

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(email=email)
            if check_password(senha, usuario.senha):
                request.session.set_expiry(timedelta(minutes=60))  # Sessão expira em 60 minutos
                request.session['email'] = email
                messages.success(request, "Logado com sucesso!")
                return redirect('dashboard')
            else:
                messages.error(request, "Senha incorreta.")
        except Usuario.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")
    context = {'form': formLogin}
    return render(request, 'form-login.html', context)

def dashboard(request):
    email = request.session.get('email')

    if not email:
        messages.error(request, "Você precisa estar logado para acessar o dashboard!")
        return redirect('appCurse')
    try:
        usuario_logado = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        messages.error(request, "Usuário não encontrado.")
        return redirect('form_login')

    context = {'dados': [usuario_logado]}
    return render(request, 'dashboard.html', context)

def editar_usuario(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    form = FormEditarUsuario(request.POST or None, instance=usuario)
    senha = request.POST.get('senha')

    if request.POST:
        if form.is_valid():
            usuario.senha = make_password(senha)
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'editar_usuario.html', context)

def excluir_usuario(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    usuario.delete()
    return redirect('exibir_users')

def add_foto(request):
    form = FormFoto(request.POST or None, request.FILES or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('galeria')
    return render(request, 'add_foto.html', {'form': form})

def galeria(request):
    email = request.session.get('email')

    if not email:
        messages.error(request, "Você precisa estar logado para acessar a galeria!")
        return redirect('form_login')

    fotos = Foto.objects.all().values()
    context = {'galeria': fotos}
    return render(request, 'galeria.html', context)

def contato(request):
    return render(request, 'contato.html')
