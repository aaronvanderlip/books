ALLOWED_HOSTS = ['.caramckenna.com', '.megmaguire.com','.smarterotica.com']
DEBUG = False

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '/home/ruralmind/webapps/2016_carabooks/carabooks/caradb.sqlite3',# Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
            }
        }

TIME_ZONE = 'America/Los_Angeles'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = '/home/ruralmind/webapps/cara_media_app/'

MEDIA_URL = '/media/'

STATIC_ROOT = '/home/ruralmind/webapps/cara_static_app/'

STATIC_URL = '///static/'

ADMIN_MEDIA_PREFIX = '/media/'

STATICFILES_DIRS = (
        )

STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        )

SECRET_KEY = 'GENERATE THIS'

TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        )

MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        )

ROOT_URLCONF = 'carabooks.urls'

TEMPLATE_DIRS = (
'/home/ruralmind/webapps/2016_carabooks/carabooks/books/templates/books/',
        )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_extensions',
    'books',
    'flatblocks',
)

LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
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
