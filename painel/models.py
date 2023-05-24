from django.db import models

class sexo(models.Model):
    description = models.TextField()
        
    def __str__(self):
        return self.description

class cliente(models.Model):
    first_name = models.CharField(max_length=50),
    email = models.CharField(max_length=50),
    password = models.CharField(max_length=255),
    sexo = models.ForeignKey(sexo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name


class user(models.Model):
    id_cliente = models.ForeignKey(cliente, null=False, blank=False, on_delete=models.CASCADE),
    user = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user
