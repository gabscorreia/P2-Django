from django import forms
from appCurse.models import Usuario, Curso, Foto

class FormCadastroUser(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome','email','senha','foto')
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control m-2', 'placeholder':'seu nome aqui'}),
            'email': forms.EmailInput(attrs={'class':'form-control m-2', 'placeholder':'usuario@email.com'}),
            'senha': forms.PasswordInput(attrs={'class':'form-control m-2'}),
            'foto': forms.FileInput(attrs={'class':'form-control m-2', 'accept':'image/*'})
        }

class FormCadastroCurso(forms.ModelForm):
    class Meta:
        model = Curso  
        fields = ('titulo', 'instrutor', 'categoria', 'duracao', 'preco', 'imagem')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Título do Curso'}),
            'instrutor': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Nome do Instrutor'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Categoria do Curso'}),
            'duracao': forms.NumberInput(attrs={'class': 'form-control m-2', 'placeholder': 'Duração em horas'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control m-2', 'step': '0.01', 'placeholder': 'Preço do Curso'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control m-2', 'accept': 'image/*'}),
        }

class FormLogin(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('email', 'senha')

        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control m-2', 'placeholder':'usuario@email.com'}),
            'senha': forms.PasswordInput(attrs={'class':'form-control m-2'})
        }

class FormEditarUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('email', 'senha')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control m-2', 'placeholder': 'usuario@email.com'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control m-2'})
        }

    def __init__(self, *args, **kwargs):
        super(FormEditarUsuario, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = True

class FormFoto(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['nome','foto']

        widgets = {
            'foto': forms.FileInput(attrs={'accept':'image/*'})
        }