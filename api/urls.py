
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
]
path('api/', include('api.urls')),
from django.urls import path
from .views import hello_view

urlpatterns = [
    path('hello/', hello_view),  # URL final será /api/hello/
]