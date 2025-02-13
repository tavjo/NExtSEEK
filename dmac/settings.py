
from __future__ import absolute_import, unicode_literals
import os

from django import VERSION as DJANGO_VERSION
from django.utils.translation import gettext_lazy as _


######################
# MEZZANINE SETTINGS #
######################

# The following settings are already defined with default values in
# the ``defaults.py`` module within each of Mezzanine's apps, but are
# common enough to be put here, commented out, for conveniently
# overriding. Please consult the settings documentation for a full list
# of settings Mezzanine implements:
# http://mezzanine.jupo.org/docs/configuration.html#default-settings

# Controls the ordering and grouping of the admin menu.
#
# ADMIN_MENU_ORDER = (
#     ("Content", ("pages.Page", "blog.BlogPost",
#        "generic.ThreadedComment", (_("Media Library"), "media-library"),)),
#     ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
#     ("Users", ("auth.User", "auth.Group",)),
# )

# A three item sequence, each containing a sequence of template tags
# used to render the admin dashboard.
#
# DASHBOARD_TAGS = (
#     ("blog_tags.quick_blog", "mezzanine_tags.app_list"),
#     ("comment_tags.recent_comments",),
#     ("mezzanine_tags.recent_actions",),
# )

# A sequence of templates used by the ``page_menu`` template tag. Each
# item in the sequence is a three item sequence, containing a unique ID
# for the template, a label for the template, and the template path.
# These templates are then available for selection when editing which
# menus a page should appear in. Note that if a menu template is used
# that doesn't appear in this setting, all pages will appear in it.

# PAGE_MENU_TEMPLATES = (
#     (1, _("Top navigation bar"), "pages/menus/dropdown.html"),
#     (2, _("Left-hand tree"), "pages/menus/tree.html"),
#     (3, _("Footer"), "pages/menus/footer.html"),
# )

# A sequence of fields that will be injected into Mezzanine's (or any
# library's) models. Each item in the sequence is a four item sequence.
# The first two items are the dotted path to the model and its field
# name to be added, and the dotted path to the field class to use for
# the field. The third and fourth items are a sequence of positional
# args and a dictionary of keyword args, to use when creating the
# field instance. When specifying the field class, the path
# ``django.models.db.`` can be omitted for regular Django model fields.
#
# EXTRA_MODEL_FIELDS = (
#     (
#         # Dotted path to field.
#         "mezzanine.blog.models.BlogPost.image",
#         # Dotted path to field class.
#         "somelib.fields.ImageField",
#         # Positional args for field class.
#         (_("Image"),),
#         # Keyword args for field class.
#         {"blank": True, "upload_to": "blog"},
#     ),
#     # Example of adding a field to *all* of Mezzanine's content types:
#     (
#         "mezzanine.pages.models.Page.another_field",
#         "IntegerField", # 'django.db.models.' is implied if path is omitted.
#         (_("Another name"),),
#         {"blank": True, "default": 1},
#     ),
# )

# Setting to turn on featured images for blog posts. Defaults to False.
#
# BLOG_USE_FEATURED_IMAGE = True

# If True, the django-modeltranslation will be added to the
# INSTALLED_APPS setting.
USE_MODELTRANSLATION = False


########################
# MAIN DJANGO SETTINGS #
########################

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [u'servername']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# If you set this to True, Django will use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en"

# Supported languages
LANGUAGES = (
    ('en', _('English')),
)

# A boolean that turns on/off debug mode. When set to ``True``, stack traces
# are displayed for error pages. Should always be set to ``False`` in
# production. Best set to ``True`` in local_settings.py
DEBUG = False

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False
#USE_I18N = True

# https://stackoverflow.com/questions/15965589/django-unicodedecodeerror-at-accounts-profiledetails-utf8-codec-cant-deco
FILE_CHARSET = "utf-8"
AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)

# The numeric mode to set newly-uploaded files to. The value should be
# a mode you'd pass directly to os.chmod.
FILE_UPLOAD_PERMISSIONS = 0o644

#############
# DATABASES #
#############

DATABASES = {
    "default": {
        # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.",
        # DB name or path to database file if using sqlite3.
        "NAME": "",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    },

    "seek": {
        # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.",
        # DB name or path to database file if using sqlite3.
        "NAME": "",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}


#########
# PATHS #
#########

# Full filesystem path to the project.
PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_APP = os.path.basename(PROJECT_APP_PATH)
PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)

# Every cache key will get prefixed with this value - here we set it to
# the name of the directory the project is in to try and use something
# project specific.
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_APP

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = "/static"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/media/"

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = "/app/media"

# Package/module name to import the root urlpatterns from for the project.
ROOT_URLCONF = "%s.urls" % PROJECT_APP

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            #os.path.join(PROJECT_ROOT, "templates"),
            #os.path.join(PROJECT_ROOT, "themes.amai.templates"),
            os.path.join(PROJECT_ROOT, "themes.SmartAdmin.templates"),
        ],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.static",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.tz",
                "mezzanine.conf.context_processors.settings",
                "mezzanine.pages.context_processors.page",
            ],
            #"builtins": [
                #"mezzanine.template.loader_tags",
            #],
            "loaders": [
                "mezzanine.template.loaders.host_themes.Loader",
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    },
]

if DJANGO_VERSION < (1, 9):
    del TEMPLATES[0]["OPTIONS"]["builtins"]

################
# APPLICATIONS #
################

INSTALLED_APPS = (
    "seek",
    'themes.SmartAdmin',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.pages",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.galleries",
    "mezzanine.twitter",
    "mezzanine.accounts",
    'widget_tweaks',

    'django_crontab',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'api_app',

)

# List of middleware classes to use. Order is important; in the request phase,
# these middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE = (
    "mezzanine.core.middleware.UpdateCacheMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    # Uncomment if using internationalisation or localisation
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.RedirectFallbackMiddleware",
    #"mezzanine.core.middleware.TemplateForDeviceMiddleware",
    #"mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

#########################
# OPTIONAL APPLICATIONS #
#########################

# These will be added to ``INSTALLED_APPS``, only if available.
OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
    "compressor",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)

##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.

# Instead of doing "from .local_settings import *", we use exec so that
# local_settings has full access to everything defined in this module.
# Also force into sys.modules so it's visible to Django's autoreload.

f = os.path.join(PROJECT_APP_PATH, "local_settings.py")
if os.path.exists(f):
    import sys
    import imp
    module_name = "%s.local_settings" % PROJECT_APP
    module = imp.new_module(module_name)
    module.__file__ = f
    sys.modules[module_name] = module
    exec(open(f, "rb").read())


####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())

# https://stackoverflow.com/questions/4438064/django-url-with-automatic-slash-adding
# https://docs.djangoproject.com/en/dev/ref/settings/#append-slash
APPEND_SLASH = False
APPEND_SLASH = True

# refer to: https://bitbucket.org/stephenmcd/mezzanine/commits/ffb536fe0d1f15f9a77a59c8c91bc5845cadc8ca
# If you set this to True, it will send new user an email with a verification link that they must click on, 
# in order to activate their account. In INSTALLED_APPS above, "mezzanine.accounts" must be active to make this work.
ACCOUNTS_VERIFICATION_REQUIRED = True
# Defaults to False and when set to True, sets newly created public user accounts to inactivate,
# requiring activation by a staff member.
ACCOUNTS_APPROVAL_REQUIRED = True
# Can contain a comma separated string of email addresses to send notification emails to
# each time a new account is created and requires activation. 
ACCOUNTS_APPROVAL_EMAILS = 'your email address'

SERVER_IPADDRESS = 'your IP address'

ALLOWED_HOSTS = ['*']
SESSION_COOKIE_DOMAIN = 'your IP address'
CSRF_TRUSTED_ORIGINS = ['server domain']

EMAIL_USE_TLS = True
EMAIL_HOST = 'your smtp server'
EMAIL_HOST_USER = 'your host email address'
EMAIL_HOST_PASSWORD = 'your host password'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'your email address'
    
# Allow specifying which database is used for a table model.
DATABASE_ROUTERS = ['seek.dbrouters.CustomRouter']

# used in dmac/views.py for managing session and authentication of user login
# SEEK_URL = "http://" + SERVER_IPADDRESS + ":3000"
NEXTSEEK_DATABASE = "default"
SEEK_HOSTNAME = "example.com"
SEEK_URL = "https://" + SEEK_HOSTNAME
SEEK_DATABASE = "seek"
SEEK_SERVER = SEEK_URL
SEEK_JS_URL = SEEK_URL

VIRTUOSO_URL = "http://" + SEEK_HOSTNAME+ ":8890/sparql/"
VIRTUOSO_JS_URL = "http://" + SEEK_HOSTNAME + ":8890/sparql"

SEEK_DATAFILE_SERVER = 'http://' + SEEK_HOSTNAME + ':portNumber'
SEEK_DATAFILE_ROOT = MEDIA_ROOT + "/uploads/"
SEEK_DATAFILE_ROOT_WEBLINK = MEDIA_URL + "uploads/"

#CRONJOBS = [
#    ('0 2 * * *', seek.cron_job.my_cron_job),
#    ('0 20 * * *', api_app.updateTrees.updateTrees)
#]

TEMPLATES_PATH = ''
TEMPLATES_PROJECT_ID = ''

AUTH_PROFILE_MODULE = "seek.User_profile"
ACCOUNTS_PROFILE_MODEL = "seek.User_profile"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "%(asctime)s %(levelname)s %(message)s",
            'datefmt': "%a, %d %b %Y %H:%M:%S"
        },
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'django.log',
            'formatter': 'verbose'
        },
        'nextseekfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'nextseek.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['logfile'],
            'propagate': True,
            'level':'DEBUG',
        },
        'dmac': {
            'handlers':['nextseekfile'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}

# PUBLISH_URL = "https://fairdomhub.org"

#refer to: https://blog.csdn.net/cuipengchong/article/details/73738416
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "%(asctime)s %(levelname)s %(message)s",
            'datefmt': "%a, %d %b %Y %H:%M:%S"
        },
    },
    'handlers': {
        'django_crontab': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'django_crontab.log',
            'formatter': 'verbose'
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'django.log',
            'formatter': 'verbose' 
        },
        'seekfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'seek.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django_crontab.crontab': {
            'handlers': ['django_crontab'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers':['logfile'],
            'propagate': True,
            'level':'DEBUG',
        },
        'seek': {
            'handlers':['seekfile'],
            'propagate': True,
            'level':'DEBUG', 
        }
    },
}

# https://newbedev.com/using-django-with-postman-detail-csrf-failed-csrf-token-missing-or-incorrect
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    #'DEFAULT_PARSER_CLASSES': [
    #    'rest_framework.parsers.JSONParser',
    #],
}
