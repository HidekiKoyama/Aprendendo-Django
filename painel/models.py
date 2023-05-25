from django.db import models

class sexo(models.Model):
    description = models.CharField(max_length=50)
        
    def __str__(self):
        return self.description
        
class clientes(models.Model):
    firstname = models.TextField(max_length=50, null=False, blank=False, default='')
    email = models.TextField(max_length=255, null=False, blank=False, default='')
    password = models.TextField(max_length=255, null=False, blank=False, default='')
    sexo = models.TextField(max_length=50)
    
    def __str__(self):
        return self.firstname


class user(models.Model):
    id_cliente = models.ForeignKey(clientes, null=False, blank=False, on_delete=models.CASCADE),
    user = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user
