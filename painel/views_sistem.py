from django.shortcuts import render
from .models import historias

def adicionar_historia(request):
    cadastrar_historias = historias()
    usuarios = str(request.POST.get("opala"))
    print(usuarios + 'aaaaaaaaaaaaaaaa')
    cadastrar_historias.id_cliente = 1
    cadastrar_historias.categoria = 1
    cadastrar_historias.titulo = request.POST.get("input-titulo-historia")
    cadastrar_historias.texto_completo = request.POST.get("input-conteudo-historia")

    cadastrar_historias.save_base()
    return render(request, 'admin/admin.html')