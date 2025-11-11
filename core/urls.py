
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'trocas', TrocaViewSet)
router.register(r'plantas', PlantaViewSet)
router.register(r'imagens', ImagemViewSet)
router.register(r'mensagens', MensagemViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
