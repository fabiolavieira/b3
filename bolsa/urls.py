from django.urls import path
from .views import home, listar_pregao, criar_pregao, listar_ativos, comprar_ativo

urlpatterns = [
    path('', home, name='home'),
    path('pregao', listar_pregao, name='listar_pregao'),
    path('novo', criar_pregao, name='criar_pregao'),
    path('ativos', listar_ativos, name='listar_ativos'),
    path('comprar/<int:id>/', comprar_ativo, name='comprar_ativo'),
    # path('vender/<int:id>/', vender_ativo, name='vender_ativo'),
]