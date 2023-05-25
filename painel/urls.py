from django.urls import path
from .views import home, admin, cadastrosex, createuser, dellsex, dellcliente

urlpatterns = [
    path('', home),
    path('admin/', admin, name='admin'),
    path('cadastrosex/', cadastrosex, name='cadastrosex'),
    path('new-user/', createuser, name='createuser'),
    path('dellsex/<int:id>/', dellsex, name='dellsex'),
    path('dellcliente/<int:id>/', dellcliente, name='dellcliente'),
]