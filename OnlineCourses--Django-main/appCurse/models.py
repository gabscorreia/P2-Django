from django.db import models

# Modelo para Usuário
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='usuarios/')

    def __str__(self):
        return self.nome

# Modelo para Curso
class Curso(models.Model):
    titulo = models.CharField(max_length=255)
    instrutor = models.CharField(max_length=255)  
    categoria = models.CharField(max_length=255)  
    duracao = models.PositiveIntegerField(help_text="Duração em horas") 
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='cursos/')  

    def __str__(self):
        return self.titulo

# Modelo para Galeria de Imagens
class Foto(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.nome
