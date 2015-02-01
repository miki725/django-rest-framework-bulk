# Bare ``settings.py`` for running tests for rest_framework_bulk

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'rest_framework_bulk.sqlite',
    }
}

MIDDLEWARE_CLASSES = ()

INSTALLED_APPS = (
    'django_nose',
    'rest_framework_bulk',
    'rest_framework_bulk.tests.simple_app',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

STATIC_URL = '/static/'
SECRET_KEY = 'foo'
