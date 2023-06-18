from django.urls import path
from .views import *
from .views_sistem import *
from django.contrib import admin

#area do administrador
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    #path('admin/pag/', admin, name='admin'),
    path('cadastrosex/', cadastrosex, name='cadastrosex'),
    path('new-user/', createuser, name='createuser'),
    path('dellsex/<int:id>/', dellsex, name='dellsex'),
    path('dellcliente/<int:id>/', dellcliente, name='dellcliente'),
    path('geral/', tela_de_login, name='tela_de_login'),
    path('dellusers/<int:id>/', dellusers, name='dellusers'),
    path('add-historia/', add_historia_tela, name='add_historia_tela'),
    path('adicionar_historia/', adicionar_historia, name='adicionar_historia'),
]