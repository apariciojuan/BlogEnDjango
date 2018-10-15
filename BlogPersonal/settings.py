import os
from django.urls import reverse_lazy

try:
    from .LocalSetting import *
    DEBUG = True
    ALLOWED_HOSTS = []
except:
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False
    ALLOWED_HOSTS = ['*']

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = KEY

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'markdownx',
    'articulos',
    'usuarios',
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

ROOT_URLCONF = 'BlogPersonal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'BlogPersonal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

LOGIN_REDIRECT_URL = reverse_lazy('articulos:list_articles')
LOGOUT_REDIRECT_URL = reverse_lazy('accounts:login')

STATIC_ROOT = os.path.join(BASE_DIR, 'BlogPersonal/staticRoot')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL ='/media/'

# Markdownify
#MARKDOWNX_MARKDOWNIFY_FUNCTION = 'markdownx.utils.markdownify' # Default function that compiles markdown using defined extensions. Using custom function can allow you to pre-process or post-process markdown text. See below for more info.

# Markdown extensions
#MARKDOWNX_MARKDOWN_EXTENSIONS = [] # List of used markdown extensions. See below for more info.
#MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS = {} # Configuration object for used markdown extensions

# Markdown urls
#MARKDOWNX_URLS_PATH = '/markdownx/markdownify/' # URL that returns compiled markdown text.
#MARKDOWNX_UPLOAD_URLS_PATH = '/markdownx/upload/' # URL that accepts file uploads, returns markdown notation of the image.

# Media path
#MARKDOWNX_MEDIA_PATH = 'markdownx/' # Path, where images will be stored in MEDIA_ROOT folder

# Image
MARKDOWNX_UPLOAD_MAX_SIZE = 12428800 # 10MB - maximum file size
MARKDOWNX_UPLOAD_CONTENT_TYPES = ['image/jpeg', 'image/png'] # Acceptable file content types
#MARKDOWNX_IMAGE_MAX_SIZE = {'size': (500, 500), 'quality': 90,} # Different options describing final image processing: size, compression etc. See below for more info.

# Editor
MARKDOWNX_EDITOR_RESIZABLE = True # Update editor's height to inner content height while typing
