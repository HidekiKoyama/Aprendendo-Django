from django.urls import path
from .views import home, admin, cadastrosex

urlpatterns = [
    path('', home),
    path('admin/', admin, name='admin'),
    path('cadastrosex/', cadastrosex, name='cadastrosex'),    
]