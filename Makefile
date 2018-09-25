coverage:
	pipenv run py.test -s --verbose --cov-report term-missing --cov-report xml --cov=pyden tests
init:
	pip install --upgrade pip pipenv
	pipenv lock
	pipenv install --dev
lint:
	pipenv run flake8 pyden
	pipenv run pydocstyle pyden
	pipenv run pylint pyden
publish:
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine upload dist/*
	rm -rf dist/ build/ .egg pyden.egg-info/
test:
	pipenv run py.test
