
# Crescer Juntos – PRO (DRF + JWT + Swagger + CORS + Filtros + Paginação)

Este backend conecta ao banco PostgreSQL já existente, gera models via `inspectdb`, cria API CRUD automaticamente e disponibiliza JWT, Swagger, CORS com credenciais, filtros, busca e ordenação, além de paginação.

## Requisitos
- Python 3.10+
- PostgreSQL 13+

## Instalação (Windows)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configurar `.env`
```env
DJANGO_SECRET_KEY=troque-este-segredo
DJANGO_DEBUG=true
DJANGO_ALLOWED_HOSTS=*
PG_DB=crecer_juntos
PG_USER=damy
PG_PASSWORD=damy2109
PG_HOST=localhost
PG_PORT=5432

# Liste origens do seu front para uso com credenciais (cookies/Authorization)
# Ex.: http://localhost:3000,https://app.seudominio.com
CORS_ALLOWED_ORIGINS=

# Páginação por padrão
API_PAGE_SIZE=20
```

## Rodar
```powershell
python manage.py migrate
python manage.py inspectdb_to_models
python manage.py generate_api_from_models
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

## Endpoints úteis
- Swagger: `GET /api/docs/`
- Redoc: `GET /api/redoc/`
- OpenAPI JSON: `GET /api/schema/`
- JWT: `POST /api/auth/token/`, `POST /api/auth/token/refresh/`, `POST /api/auth/token/verify/`
- CRUD: `/api/<tabela>/`
  - Filtros: `?campo=valor`
  - Busca: `?search=texto` (em campos textuais)
  - Ordenação: `?ordering=campo` ou `?ordering=-campo`
  - Paginação: `?page=2` (tamanho por `API_PAGE_SIZE`)

## Produção (recomendações)
- `DJANGO_DEBUG=false`
- `DJANGO_ALLOWED_HOSTS` definido
- Defina `CORS_ALLOWED_ORIGINS` com domínios do front e mantenha `CORS_ALLOW_CREDENTIALS=True`
- SECRET_KEY forte e exclusivo
- Considere ativar rotação e blacklist de refresh tokens no SimpleJWT
- Restrinja permissões dos ViewSets conforme regras do negócio
