import os
import environ
env = environ.Env()
environ.Env.read_env("../democelery/.env")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'ayp&32$asp3!-3dqnen9km97r+oag5&7)+*=t5r%7q56ocwgor'
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'democelery.security',
    'democelery.network',
    'widget_tweaks'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'democelery.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'democelery.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': env("DB_HOST"),
        'NAME': env("DB_NAME"),
        'USERNAME': env("DB_USERNAME"),
        'PASSWORD': env("DB_PASSWORD"),
        'PORT': env("DB_PORT"),
    }
}

EMAIL_USE_TLS = env("EMAIL_USE_TLS")
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
EMAIL_BACKEND = env("EMAIL_BACKEND")


LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/accounts/login/"
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


__STATIC_PATH = os.path.dirname(os.path.dirname(__file__))

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(__STATIC_PATH, "democelery/static"),
)
STATIC_ROOT = os.path.join(__STATIC_PATH, '../static')


# Celery Configuration Options
CELERY_TIMEZONE = "America/Merida"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

# Celery beat
from democelery.celery import app
from celery.schedules import timedelta, crontab


app.conf.beat_schedule = {
    'delete_logs': {
        'task': 'democelery.network.tasks.delete_log',
        'schedule': timedelta(seconds=5),
    }
}

app.conf.timezone = CELERY_TIMEZONE

