from .base import * 
from core.env import env

DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = env('ALLOWED_HOSTS', default=['*'])
