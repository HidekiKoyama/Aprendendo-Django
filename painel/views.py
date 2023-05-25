from django.shortcuts import render
from painel.models import sexo, clientes, user

def home(request):
    return render(request, 'realiza-login/index.html')

def alterasexo(request):
    return render(request, '/admin/alter_sex/altersex.html')

def admin(request):
    cad_sexo = sexo.objects.all()
    return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo})

def cadastrosex(request):
    nome_cad = request.POST.get("nome"),
    sexo.objects.create(description = nome_cad),
    nome = sexo.objects.all(),

    return render(request, 'admin/admin.html' , {'cad_sexo': nome})

# carrega tabela sex
def tablesex (request):
    cad_sexo = sexo.objects.all()
    return render(request, 'cadastrar-user/index.html' , {'cad_sexo': cad_sexo})

def rcreateuser(request):
    nome = clientes.objects.all(),
    return render(request, 'cadastrar-user/index.html' , {'cad_sexo': nome})    

def createuser(request):
    nome_cad = request.POST.get("nome"),
    clientes.objects.create(firstname = nome_cad),
    nome = clientes.objects.all(),

    return render(request, 'cadastrar-user/index.html' , {'cad_sexo': nome})