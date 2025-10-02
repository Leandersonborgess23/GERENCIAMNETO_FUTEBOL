import secrets
from datetime import timedelta


class Config:
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///gerenciamento_futebol.db'
    SESSION_COOKIE_HTTPONLY=True
    SESSION_COOKIE_SAMESITE="Lax"
    SESSION_COOKIE_SECURE=False
    REMEMBER_COOKIE_DURATION=timedelta(days=7)