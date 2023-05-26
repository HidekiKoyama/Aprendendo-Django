from django.db import models

class sexo(models.Model):
    descricao = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.descricao        
        
class clientes(models.Model):
    nome = models.TextField(max_length=50, null=False, blank=False)
    email = models.TextField(max_length=255, null=False, blank=False, default='')
    sexo = models.ForeignKey(sexo, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome, self.email, self.senha, self.sexo

class user(models.Model):
    id_cliente = models.ForeignKey(clientes, null=False, blank=False, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
