from os import path

PROJECT_HOME = path.abspath(path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']

ADMINS = (
    ('Szymon Kulinski', 'szymon.kulinski@zhr.pl'),
    ('Jacek Tomaszewski', 'jacek.tomek@gmail.com'),
)
MANAGERS = ADMINS

APPEND_SLASH = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'market',
        'USER': 'adrian',
        'PASSWORD': 'adrian',
        'HOST': '127.0.0.1',
        #'PORT': '',
    }
}


#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': '',
#        'USER': '',
#        'PASSWORD': '',
#        'HOST': '',
#        'PORT': '',
#    }
#}



TIME_ZONE = 'Europe/Warsaw'
LANGUAGE_CODE = 'pl'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

RECAPTCHA_PUBLIC_KEY = '6Le60OsSAAAAAOH-gR_t52sqLkn75CRPS09shpKO'
RECAPTCHA_PRIVATE_KEY = '6Le60OsSAAAAAONFPpog2epgi1e-AabCj7EixXhQ'

MEDIA_ROOT = path.join(PROJECT_HOME, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = path.join(PROJECT_HOME, 'servestatic')
STATIC_URL = '/static/'

ROOT_URLCONF = 'supermarketmetodyczny.urls'
WSGI_APPLICATION = 'supermarketmetodyczny.wsgi.application'

STATICFILES_DIRS = (
    path.join(PROJECT_HOME, 'static'),
)
TEMPLATE_DIRS = (
    path.join(PROJECT_HOME, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
SECRET_KEY = '6sk&j_utdt6h3*u(!0^y^@(n=3=$b@#qgw$9s^274)-d#j&^tr'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    # 'admin_tools',
    #    'admin_tools.theming',
    #    'admin_tools.menu',
    #    'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'orderable',
    'django_js_reverse',
    'polymorphic',
    'django.contrib.contenttypes',
    'captcha',
    'tinymce',
    'base',
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

ADMIN_TOOLS_MENU = 'supermarketmetodyczny.menu.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'supermarketmetodyczny.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'supermarketmetodyczny.dashboard.CustomAppIndexDashboard'

ORDERABLE_ORDER_EDITABLE = False

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/logowanie/'
LOGOUT_URL = '/wylogowanie/'

SOUTH_MIGRATION_MODULES = {
        'captcha': 'captcha.south_migrations',
}

try:
    from prod_settings import *
except ImportError:
    pass


TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
	'nowrap': True
}


