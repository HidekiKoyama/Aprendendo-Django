from django.shortcuts import render, redirect
from painel.models import sexo, clientes, user

def home(request):
    return render(request, 'realiza-login/index.html')

def admin(request):
    cad_sexo = sexo.objects.all()
    cliente = clientes.objects.all()
    return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cliente': cliente})

def cadastrosex(request):
    nome_cad = request.POST.get("nome"),
    sexo.objects.create(description = nome_cad),
    nome = sexo.objects.all(),
    return render(request, 'admin/admin.html', {'cad_sexo': nome})


#insert into clientes
def createuser(request):
    nome_cad = request.POST.get("nome"),
    senha = request.POST.get("password"),
    clientes.objects.create(firstname = nome_cad, password = senha),
    nome = clientes.objects.all(),

    return render(request, 'cadastrar-user/index.html' , {'cad_sexo': nome})


# Deleta dados

def dellsex(request, id):
    deletar = sexo.objects.get(id=id)
    deletar.delete()
    cad_sexo = sexo.objects.all()
    cliente = clientes.objects.all()
    return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cliente': cliente})


def dellcliente(request, id):
    deletar = clientes.objects.get(id=id)
    deletar.delete()
    cad_sexo = sexo.objects.all()
    cliente = clientes.objects.all()
    return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cliente': cliente})


""""
def deleta(request):
    id_do_fera = request.POST.get("<id:id>")
    SD1010.objects.delete(id=id_do_fera)
    nome = SD1010.objects.all()
    return render(request, "index.html", {"cliente": nome})
"""""