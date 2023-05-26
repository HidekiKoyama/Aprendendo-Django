from django.shortcuts import render
from painel.models import sexo, clientes#, user
import sqlite3 as sql
import pandas

def home(request):
    return render(request, 'realiza-login/index.html')

def admin(request): 
    try:
        cad_sexo = sexo.objects.all()
        cad_cliente = clientes.objects.all()
        return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cad_cliente': cad_cliente})
    except:
        return render(request, 'admin/admin.html')

def cadastrosex(request):
    cadastrar_sex = sexo()
    cadastrar_sex.descricao = request.POST.get('nome')
    cadastrar_sex.save_base()

    cad_sexo = sexo.objects.all()
    cliente = clientes.objects.all()
    return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cliente': cliente})


#insert into clientes
def createuser(request):
    try:
        insert_into_cad_cliente = clientes()
        #insert_into_nick_user = user()

        #insert_into_nick_user.id_cliente = ()
        #user_cad = request.POST.get('user_cad') outra tabela
        

        insert_into_cad_cliente.nome = request.POST.get('nome_cad')
        insert_into_cad_cliente.email = request.POST.get('email_cad')
        insert_into_cad_cliente.senha = request.POST.get('password_cad')
        
        #depois transformar em funbcao para melhorar o codigo

        conexao = sql.connect("db.sqlite3")
        filtro = request.POST.get('sexo_cad')
        df = pandas.read_sql_query(f"SELECT id FROM painel_sexo WHERE descricao = '{filtro}'", conexao)
        val = int(df.iloc[0:1].values)
        print(val)
        insert_into_cad_cliente.sexo = val
        val = int(df.iloc[0:1].values)

        insert_into_cad_cliente.save_base()

        cad_sexo = sexo.objects.all()
        cliente = clientes.objects.all()
        return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cliente': cliente})
    except:
        list_sex = sexo.objects.all()
        cliente = clientes.objects.all()
        return render(request, 'cadastrar-user/index.html' , {'list_sex': list_sex, 'cliente': cliente})

    # Deleta dados

def dellsex(request, id):
    try:
        deletar = sexo.objects.get(id=id)
        deletar.delete()
        cad_sexo = sexo.objects.all()
        cliente = clientes.objects.all()
        return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cliente': cliente})
    except:
        cad_sexo = sexo.objects.all()
        cliente = clientes.objects.all()
        return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cliente': cliente})



def dellcliente(request, id):
    
    try:
        deletar = clientes.objects.get(id=id)
        deletar.delete()
        cad_sexo = sexo.objects.all()
        cliente = clientes.objects.all()
        return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cliente': cliente})
    except:
        cad_sexo = sexo.objects.all()
        cliente = clientes.objects.all()
        return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cliente': cliente})


def tela_de_login(request):
    solicita_login = request.POST.get('usuario')
    solicita_senha = request.POST.get('senha')

    try:
        conexao = sql.connect('db.sqlite3')
        valida_filtro_user = solicita_login
        valida_filtro_senha = solicita_senha

        df = pandas.read_sql_query(f'SELECT id painel_clientes JOIN (SELECT painel_user WHERE user = {valida_filtro_user} )'+
                                   f'WHERE senha = {valida_filtro_senha}', conexao)
        
        val = int(df.iloc[0:1].values)
        val != ''
        return render(request, 'sistema/tela_de_inicio.html')
    except:
        return render(request, 'realiza-login/index.html')



""""
def deleta(request):
    id_do_fera = request.POST.get("<id:id>")
    SD1010.objects.delete(id=id_do_fera)
    nome = SD1010.objects.all()
    return render(request, "index.html", {"cliente": nome})
"""""