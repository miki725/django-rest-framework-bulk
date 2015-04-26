.PHONY: clean-pyc clean-build docs clean

TEST_FLAGS=--verbosity=2
COVER_FLAGS=--source=rest_framework_bulk

help:
	@echo "install - install all requirements including for testing"
	@echo "install-quite - same as install but pipes all output to /dev/null"
	@echo "clean - remove all artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "clean-test-all - remove all test-related artifacts including tox"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-coverage - run tests with coverage report"
	@echo "test-all - run tests on every Python version with tox"
	@echo "check - run all necessary steps to check validity of project"
	@echo "release - package and upload a release"
	@echo "dist - package"

install:
	pip install -r requirements-dev.txt

install-quite:
	pip install -r requirements-dev.txt > /dev/null

clean: clean-build clean-pyc clean-test-all

clean-build:
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info

clean-pyc:
	-@find . -name '*.pyc' -follow -print0 | xargs -0 rm -f
	-@find . -name '*.pyo' -follow -print0 | xargs -0 rm -f
	-@find . -name '__pycache__' -type d -follow -print0 | xargs -0 rm -rf

clean-test:
	rm -rf .coverage coverage*
	rm -rf tests/.coverage test/coverage*
	rm -rf htmlcov/

clean-test-all: clean-test
	rm -rf .tox/

lint:
	flake8 rest_framework_bulk

test:
	python tests/manage.py test ${TEST_FLAGS}

test-coverage: clean-test
	-coverage run ${COVER_FLAGS} tests/manage.py test ${TEST_FLAGS}
	@exit_code=$?
	@-coverage report
	@-coverage html
	@exit ${exit_code}

test-all:
	tox

check: clean-build clean-pyc clean-test lint test

release: clean
	python setup.py sdist upload

dist: clean
	python setup.py sdist
	ls -l dist
