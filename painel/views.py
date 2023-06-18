from django.shortcuts import render
from painel.models import sexo, clientes, user

def home(request):
    return render(request, 'realiza-login/index.html')
    
def cadastrosex(request):
    cadastrar_sex = sexo()
    cadastrar_sex.descricao = request.POST.get('nome')
    cadastrar_sex.save_base()
    cad_sexo = sexo.objects.all()
    cad_cliente = clientes.objects.all()
    cad_users = user.objects.all()
    return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cad_cliente': cad_cliente, 'cad_users': cad_users})


#insert into clientes
def createuser(request):
    if request.method != 'POST': 
        list_sex = sexo.objects.all()
        return render(request, 'cadastrar-user/index.html' , {'list_sex': list_sex})
    else:
        try:
            insert_into_cad_cliente = clientes()
            

            insert_into_cad_cliente.nome = request.POST.get('nome_cad')
            insert_into_cad_cliente.email = request.POST.get('email_cad')
            insert_into_cad_cliente.senha = request.POST.get('password_cad')
            insert_into_cad_cliente.save_base()
            insert_into_nick_user = user()
            insert_into_nick_user.id_cliente = val
            insert_into_nick_user.user = request.POST.get('user_cad')
            insert_into_nick_user.save_base()
            return render(request, 'realiza-login/index.html')
        except:
            list_sex = sexo.objects.all()
            return render(request, 'cadastrar-user/index.html' , {'list_sex': list_sex, 'tipoerro': 'Usuário ou email já registrado'})

# Deleta dados

def dellsex(request, id):
    try:
        deletar = sexo.objects.get(id=id)
        deletar.delete()
        cad_sexo = sexo.objects.all()
        cad_cliente = clientes.objects.all()
        cad_users = user.objects.all()
        return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cad_cliente': cad_cliente, 'cad_users': cad_users})
    except:
        cad_sexo = sexo.objects.all()
        cad_cliente = clientes.objects.all()
        cad_users = user.objects.all()
        return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cad_cliente': cad_cliente, 'cad_users': cad_users})



def dellcliente(request, id):
    
    try:
        deletar = clientes.objects.get(id=id)
        deletar.delete()
        cad_sexo = sexo.objects.all()
        cad_cliente = clientes.objects.all()
        cad_users = user.objects.all()
        return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cad_cliente': cad_cliente, 'cad_users': cad_users})
    except:
        cad_sexo = sexo.objects.all()
        cad_cliente = clientes.objects.all()
        cad_users = user.objects.all()
        return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cad_cliente': cad_cliente, 'cad_users': cad_users})

def dellusers(request, id):
    deletar = user.objects.get(id=id)
    deletar.delete()
    cad_sexo = sexo.objects.all()
    cad_cliente = clientes.objects.all()
    cad_users = user.objects.all()
    return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cad_cliente': cad_cliente, 'cad_users': cad_users})

def tela_de_login(request):
    solicita_login = request.POST.get('usuario')
    solicita_senha = request.POST.get('senha')

    try:
        conexao = sql.connect('db.sqlite3')
        df = pandas.read_sql_query("SELECT pn_cliente.senha, pn_user.user7"+
            "FROM painel_clientes pn_cliente " +
            f"JOIN(SELECT user, id_cliente FROM painel_user WHERE user = '{solicita_login}') pn_user "+
            F"ON pn_cliente.id = pn_user.id_cliente WHERE pn_cliente.senha = '{solicita_senha}'", conexao)

        aval = df.iloc[0:1].values
        print(aval)
        if (solicita_login in aval and solicita_senha in aval):
            if(solicita_login == 'admin'):
                cad_sexo = sexo.objects.all()
                cad_cliente = clientes.objects.all()
                cad_users = user.objects.all()
                return render(request, 'admin/admin.html' , {'cad_sexo': cad_sexo, 'cad_cliente': cad_cliente, 'cad_users': cad_users})
            else:
                return render(request, 'sistema/tela_de_inicio.html', {'pessoa': solicita_login})
        else:
            return render(request, 'sistema/tela_de_inicio.html')    
    except:
        return render(request, 'sistema/tela_de_inicio.html')

# TELA DE
def add_historia_tela(request):
    return render (request, 'sistema/add-historia-tela.html')

""""
def deleta(request):
    id_do_fera = request.POST.get("<id:id>")
    SD1010.objects.delete(id=id_do_fera)
    nome = SD1010.objects.all()
    return render(request, "index.html", {"cliente": nome})
"""