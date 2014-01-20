"""
Based on Django REST Framework's ``setup.py``.
"""
import os
from setuptools import setup
from rest_framework_bulk import __version__, __author__


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])

    if filepaths:
        return {package: filepaths}
    else:
        return None


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='djangorestframework-bulk',
    version=__version__,
    author=__author__,
    author_email='miroslav@miki725.com',
    description='Django REST Framework bulk CRUD view mixins',
    long_description=read('README.rst') + read('LICENSE.rst'),
    url='https://github.com/miki725/django-rest-framework-bulk',
    license='MIT',
    keywords='django',
    packages=get_packages('rest_framework_bulk'),
    data_files=get_package_data('rest_framework_bulk'),
    install_requires=[
        'django',
        'djangorestframework',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: MIT License',
    ],
)
