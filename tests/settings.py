# Bare ``settings.py`` for running tests for rest_framework_bulk

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'rest_framework_bulk.sqlite'
    }
}

INSTALLED_APPS = (
    'django_nose',
    'rest_framework_bulk',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = (
    '--all-modules',
    '--with-doctest',
    '--with-coverage',
    '--cover-package=rest_framework_bulk',
)

STATIC_URL = '/static/'
SECRET_KEY = 'foo'
