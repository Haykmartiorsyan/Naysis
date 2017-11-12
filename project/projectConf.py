

def createSettings(name,password):
    settingsPath = "/srv/envs/naysis/src/{name}/Enamra/settings.py".format(name=name)
    settingsFile = open(settingsPath, 'w+')

    settingsString =""

    settingsString +="import os\n"
    settingsString+="# Build paths inside the project like this: os.path.join(BASE_DIR, ...)\n" \
                    "BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n"

    settingsString+="# Quick-start development settings - unsuitable for production\n" \
                    "# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/\n" \
                    "# SECURITY WARNING: keep the secret key used in production secret!\n" \
                    "SECRET_KEY = 'vs&cv%d3pkk+y#$yuw^4a3#8q4tn95%&y0n#)q)so!qre6yhko'\n\n"

    settingsString+="# SECURITY WARNING: don't run with debug turned on in production!\n" \
                    "DEBUG = False\n" \
                    "ALLOWED_HOSTS = ['*']\n\n"

    settingsString+="AUTH_USER_MODEL='myuser.MyUser'\n" \
                    "ACCOUNT_USER_MODEL_USERNAME_FIELD = None\n" \
                    "ACCOUNT_EMAIL_REQUIRED = True\n" \
                    "ACCOUNT_USERNAME_REQUIRED = False\n" \
                    "ACCOUNT_AUTHENTICATION_METHOD = 'email'\n\n"

    settingsString+="EMAIL_USE_TLS = True\n" \
                    "EMAIL_HOST = 'smtp.gmail.com'\n" \
                    "EMAIL_PORT = 587\n" \
                    "EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = 'example@naysis.com' \n" \
                    "EMAIL_HOST_PASSWORD = 'examplepass' \n" \
                    "EMAIL_ADMIN = 'example@naysis.com' \n\n"

    settingsString+="CART_SESSION_ID = 'cart'\n" \
                    "WISHLIST_SESSION_ID = 'wishlist'\n" \
                    "LOGIN_REDIRECT_URL = '/profile'\n\n"

    settingsString+="# Application definition\n" \
                    "INSTALLED_APPS = [\n" \
                    "\t'accounts',\n" \
                    "\t'Enamra',\n" \
                    "\t'SisianShop',\n" \
                    "\t'myuser',\n" \
                    "\t'estore',\n" \
                    "\t'ecart',\n" \
                    "\t'Blog',\n" \
                    "\t'MediaManagement',\n" \
                    "\t'Portfolio',\n" \
                    "\t'paypal.standard.ipn',\n" \
                    "\t'payment',\n" \
                    "\t'orders',\t" \
                    "\t'django.contrib.sites',\n" \
                    "\t'allauth',\n" \
                    "\t'allauth.account',\n" \
                    "\t'allauth.socialaccount',\n" \
                    "\t'allauth.socialaccount.providers.facebook',\n" \
                    "\t'django.contrib.admin',\n" \
                    "\t'django.contrib.auth',\n" \
                    "\t'django.contrib.contenttypes',\n" \
                    "\t'django.contrib.sessions',\n" \
                    "\t'django.contrib.messages',\n" \
                    "\t'django.contrib.staticfiles',\n" \
                    "\t'estore.templatetags.arrayextras',\n" \
                    "]\n\n"

    settingsString+="PAYPAL_TEST = True\n" \
                    "PAYPAL_RECEIVER_EMAIL = 'example@naysis.com' \n\n"

    settingsString+="MIDDLEWARE = [\n" \
                    "\t'django.middleware.security.SecurityMiddleware',\n" \
                    "\t'django.contrib.sessions.middleware.SessionMiddleware',\n" \
                    "\t'django.middleware.common.CommonMiddleware',\n" \
                    "\t'django.middleware.csrf.CsrfViewMiddleware',\n" \
                    "\t'django.contrib.auth.middleware.AuthenticationMiddleware',\n" \
                    "\t'django.contrib.messages.middleware.MessageMiddleware',\n" \
                    "\t'django.middleware.clickjacking.XFrameOptionsMiddleware',\n" \
                    "]\n\n"

    settingsString+="ROOT_URLCONF = 'Enamra.urls'\n\n"

    settingsString+="TEMPLATES = [\n" \
                    "\t{\n" \
                    "\t\t'BACKEND': 'django.template.backends.django.DjangoTemplates',\n" \
                    "\t\t'DIRS': [],\n" \
                    "\t\t'APP_DIRS': True,\n" \
                    "\t\t'OPTIONS': {\n" \
                    "\t\t\t'context_processors': [\n" \
                    "\t\t\t\t'django.template.context_processors.debug',\n" \
                    "\t\t\t\t'django.template.context_processors.request',\n" \
                    "\t\t\t\t'django.contrib.auth.context_processors.auth',\n" \
                    "\t\t\t\t'django.contrib.messages.context_processors.messages',\n" \
                    "\t\t\t\t'estore.estore_context_proc.loadContent',\n" \
                    "\t\t\t\t'estore.estore_context_proc.loadSlider',\n" \
                    "\t\t\t\t'estore.estore_context_proc.theMenu',\n" \
                    "\t\t\t\t'ecart.context_processors.cart',\n" \
                    "\t\t\t\t'estore.estore_context_proc.getProductSlidersData',\n" \
                    "\t\t\t\t'SisianShop.sisian_shop_context_processor.getAlerts',\n" \
                    "\t\t\t],\n" \
                    "\t\t},\n" \
                    "\t},\n" \
                    "]\n\n"

    settingsString+="AUTHENTICATION_BACKENDS = (\n" \
                    "\t'django.contrib.auth.backends.ModelBackend',\n" \
                    "\t'allauth.account.auth_backends.AuthenticationBackend',\n" \
                    ")\n\n"


    settingsString+="WSGI_APPLICATION = 'Enamra.wsgi.application'\n\n"

    settingsString+="# Database\n" \
                    "# https://docs.djangoproject.com/en/1.10/ref/settings/#databases\n\n"


    settingsString+="DATABASES = {{\n" \
                    "\t'default': {{\n" \
                    "\t\t'ENGINE': 'django.db.backends.mysql',\n" \
                    "\t\t'NAME': 'naysis_{name}',\n" \
                    "\t\t'USER': '{name}_user',\n" \
                    "\t\t'PASSWORD': '{password}',\n" \
                    "\t\t'HOST': '104.236.46.24',\n" \
                    "\t\t'PORT': '2268',\t" \
                    "\t\t'OPTIONS': {{\n" \
                    "\t\t\t'init_command': \"SET sql_mode='STRICT_TRANS_TABLES'\",\n" \
                    "\t\t\t'charset': 'utf8mb4',\n" \
                    "\t\t}},\n" \
                    "\t}},\n" \
                    "}}\n\n".format(name=name,password=password)


    settingsString+="# Password validation\n" \
                    "# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators\n"

    settingsString+="AUTH_PASSWORD_VALIDATORS = [\n" \
                    "\t{\n" \
                    "\t\t'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',\n" \
                    "\t},\n" \
                    "\t{\n" \
                    "\t\t'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',\n" \
                    "\t},\n" \
                    "\t{\n" \
                    "\t\t'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',\n" \
                    "\t},\n" \
                    "\t{\n" \
                    "\t\t'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',\n" \
                    "\t},\n" \
                    "]\n\n"

    settingsString+="# Internationalization\n" \
                    "# https://docs.djangoproject.com/en/1.10/topics/i18n/\n" \
                    "LANGUAGE_CODE = 'en-us'\n" \
                    "TIME_ZONE = 'UTC'\n" \
                    "USE_I18N = True\n" \
                    "USE_L10N = True\n" \
                    "USE_TZ = False\n" \
                    "SILENCED_SYSTEM_CHECKS = [\n" \
                    "\t'django_mysql.W002',\n" \
                    "]\n\n"

    settingsString+="# Static files (CSS, JavaScript, Images)\n" \
                    "MEDIA_ROOT = os.path.join(BASE_DIR, 'media')\n" \
                    "MEDIA_URL = '/media/'\n" \
                    "STATIC_URL = '/static/'\n" \
                    "STATIC_ROOT = os.path.join(BASE_DIR, 'Enamra/static')\n" \
                    "STATICFILES_DIRS = [\n" \
                    "\tos.path.join(BASE_DIR, 'Enamra/static_bk'),\n" \
                    "]\n\n" \
                    "SITE_ID = 2\n"

    settingsFile.write(settingsString)
    settingsFile.close()





def createWsgi(name):
    wsgiPath = "/srv/envs/naysis/src/{name}/Enamra/wsgi.py".format(name=name)
    wsgiFile = open(wsgiPath, 'w+')



    wsgiString=""

    wsgiString+="import os, sys\n" \
                "sys.path.append('/srv/envs/naysis/lib/python3.5/site-packages')\n" \
                "from django.core.wsgi import get_wsgi_application\n" \
                "sys.path.append('/srv/envs/naysis/src/{name}')\n" \
                "os.environ['DJANGO_SETTINGS_MODULE'] = 'Enamra.settings'\n" \
                "application = get_wsgi_application()\n".format(name=name)


    wsgiFile.write(wsgiString)
    wsgiFile.close()





















