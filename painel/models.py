from django.db import models

class sexo(models.Model):
    descricao = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.descricao        
        
class clientes(models.Model):
    nome = models.TextField(max_length=50, null=False, blank=False)
    email = models.TextField(max_length=255, null=False, blank=False, default='', unique=True)
    senha = models.CharField(max_length=255, default=12345)
    sexo = models.IntegerField()

    def __str__(self):
        return self.nome, self.email, self.senha, self.sexo

class user(models.Model):
    id_cliente = models.IntegerField()
    user = models.CharField(max_length=50, unique=True)
