install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

gendiff-help:
	poetry run gendiff -h

gendiff:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

test:
	poetry run pytest 

test-coverage:
	poetry run pytest --cov --cov-report term-missing --cov-report xml

.PHONY: install package-install build  package-reinstall lint gendiff-help gendiff test