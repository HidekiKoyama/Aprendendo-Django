from django.urls import path
from .views import home, admin, cadastrosex, createuser, rcreateuser

urlpatterns = [
    path('', home),
    path('admin/', admin, name='admin'),
    path('cadastrosex/', cadastrosex, name='cadastrosex'),
    path('new-user/', createuser, name='createuser'),
    path('new-user/', rcreateuser, name='rcreateuser'),
]