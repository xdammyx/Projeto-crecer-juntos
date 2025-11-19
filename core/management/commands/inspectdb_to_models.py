
from django.core.management.base import BaseCommand
from django.core.management import call_command
from io import StringIO
from pathlib import Path

class Command(BaseCommand):
    help = 'Gera core/models.py a partir do banco de dados (inspectdb).'

    def handle(self, *args, **options):
        out = StringIO()
        self.stdout.write(self.style.WARNING('Executando inspectdb...'))
        call_command('inspectdb', stdout=out)
        code = out.getvalue()
        target = Path(__file__).resolve().parents[2] / 'core' / 'models.py'
        header = ('"""
Modelos gerados via inspectdb. Ajuste conforme necessário.
'                   'Por padrão, Meta.managed=False para tabelas já existentes.
'                   '"""
')
        target.write_text(header + code, encoding='utf-8')
        self.stdout.write(self.style.SUCCESS(f'Modelos escritos em {target}'))
