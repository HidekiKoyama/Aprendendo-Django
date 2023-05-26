from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('admin/', admin, name='admin'),
    path('cadastrosex/', cadastrosex, name='cadastrosex'),
    path('new-user/', createuser, name='createuser'),
    path('dellsex/<int:id>/', dellsex, name='dellsex'),
    path('dellcliente/<int:id>/', dellcliente, name='dellcliente'),
    path('geral/', tela_de_login, name='tela_de_login'),
    path('dellusers/<int:id>/', dellusers, name='dellusers'),
    path('newuser/', redireciona_cad_user, name='redireciona_cad_user'),
]