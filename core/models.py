
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=40)
    email = models.EmailField(unique=True, max_length=80)
    senha = models.CharField(max_length=15)
    localizacao = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateField(auto_now_add=True)

class Troca(models.Model):
    data = models.DateField()
    status = models.CharField(max_length=15)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Planta(models.Model):
    nome_popular = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    origem = models.CharField(max_length=80)
    familia = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.CharField(max_length=150)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Imagem(models.Model):
    url_imagem = models.CharField(max_length=150)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name='galeria')

class Mensagem(models.Model):
    mensagem = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Avaliacao(models.Model):
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    data_hora = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(blank=True, null=True)
    avaliador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='avaliacoes_feitas')
    avaliado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='avaliacoes_recebidas')
