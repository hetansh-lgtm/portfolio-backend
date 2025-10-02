# Portfolio Backend (Django + DRF)

## Quickstart
```bash
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

API:
- `GET /api/v1/projects/`
- `POST /api/v1/contact/`

### Env & CORS
- Set `DJANGO_ALLOWED_HOSTS` to include your backend domain, e.g. `api.yourdomain.com`.
- Set `CORS_ALLOWED_ORIGINS` to include your frontend origins, e.g. `https://www.yourdomain.com,http://localhost:5173`.

### Deploying
- Use the provided `Procfile` for platforms like Railway/Heroku.
- Configure Postgres and environment variables per `.env.example`.