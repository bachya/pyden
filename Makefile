ci:
	pipenv run py.test --junitxml=report.xml
coverage:
	pipenv run py.test -s --verbose --cov-report term-missing --cov-report xml --cov=pyden tests
docs:
	cd docs && make html
init:
	pip install --upgrade pip pipenv
	pipenv lock
	pipenv install --dev
lint:
	pipenv run pylint pyden
	pipenv run flake8 pyden
	pipenv run pydocstyle pyden
publish:
	python setup.py sdist bdist_wheel
	pipenv run twine upload dist/*
	rm -rf dist/ build/ .egg pyden.egg-info/
test:
	pipenv run detox
