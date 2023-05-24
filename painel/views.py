from django.shortcuts import render
from painel.models import sexo

def home(request):
    return render(request, 'realiza-login/index.html')

def admin(request):
    nome = sexo.objects.all(),
    return render(request, 'admin/admin.html' , {"cliente": nome})

def cadastrosex(request):
    nome_cad = request.POST.get("nome"),
    sexo.objects.create(description = nome_cad),
    nome = sexo.objects.all(),
    return render(request, 'admin/admin.html' , {"cliente": nome})


'''

def cadastrosex(request):
    nome_cad = request.POST.get("nome")
    sexo.objects.create(descripition=nome_cad)
    nome = sexo.objects.all()
    return render(request, './realiza-login/index.html' , {"cliente": nome})

'''

    #SD1010.objects.create(nome=novo_nome)
    # nome, senha, user e email
