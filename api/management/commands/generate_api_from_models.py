
from django.core.management.base import BaseCommand
from django.apps import apps
from pathlib import Path
import re
from django.db import models as dj_models

class Command(BaseCommand):
    help = 'Gera serializers, viewsets e urls com filtros, ordenação e busca para todos os models do app core.'

    def handle(self, *args, **options):
        models = list(apps.get_app_config('core').get_models())
        if not models:
            self.stderr.write(self.style.ERROR('Nenhum modelo encontrado em core. Execute primeiro inspectdb_to_models.'))
            return

        api_dir = Path(__file__).resolve().parents[2] / 'api'
        serializers_path = api_dir / 'serializers.py'
        views_path = api_dir / 'views.py'
        urls_path = api_dir / 'urls.py'

        ser_lines = [
            'from rest_framework import serializers',
            'from core import models as core_models',
            '',
        ]

        view_lines = [
            'from rest_framework import viewsets, permissions',
            'from core import models as core_models',
            'from .serializers import *',
            '',
        ]

        url_lines = [
            'from django.urls import path, include',
            'from rest_framework.routers import DefaultRouter',
            'from .views import *',
            '',
            'router = DefaultRouter()',
            '',
        ]

        for m in models:
            name = m.__name__
            # snake_case para rota
            base = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

            # campos para filtros e busca
            fields = [f.name for f in m._meta.get_fields() if hasattr(f, 'attname')]
            search_fields = [f.name for f in m._meta.fields if isinstance(f, (dj_models.CharField, dj_models.TextField))]

            # Serializer
            ser_lines += [
                f'class {name}Serializer(serializers.ModelSerializer):',
                '    class Meta:',
                f'        model = core_models.{name}',
                "        fields = '__all__'",
                '',
            ]

            # ViewSet com filtros, busca e ordenação
            view_lines += [
                f'class {name}ViewSet(viewsets.ModelViewSet):',
                f'    queryset = core_models.{name}.objects.all()',
                f'    serializer_class = {name}Serializer',
                '    permission_classes = [permissions.IsAuthenticatedOrReadOnly]',
                f'    filterset_fields = {fields!r}',
                f'    search_fields = {search_fields!r}',
                "    ordering_fields = '__all__'",
                '',
            ]

            # Rota
            url_lines += [
                f"router.register(r'{base}', {name}ViewSet, basename='{base}')",
            ]

        url_lines += ['', 'urlpatterns = [', "    path('', include(router.urls)),", ']']

        serializers_path.write_text('
'.join(ser_lines) + '
', encoding='utf-8')
        views_path.write_text('
'.join(view_lines) + '
', encoding='utf-8')
        urls_path.write_text('
'.join(url_lines) + '
', encoding='utf-8')

        self.stdout.write(self.style.SUCCESS('API gerada com filtros, busca e ordenação.'))
